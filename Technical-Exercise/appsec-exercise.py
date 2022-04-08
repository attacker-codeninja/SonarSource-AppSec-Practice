from flask import Flask, request, flash, redirect, render_template, render_template_string, url_for, send_file
from database import db
from database.users import User, is_username_available, user_with_username
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from forms import RegistrationForm, LoginForm, EditProfileForm
import settings
import json
import os
import hashlib
import pathlib


def create_app():
    flask_app = Flask(__name__)
    configure_app(flask_app)
    db.init_app(flask_app)
    configure_login_manager(flask_app)
    return flask_app


def configure_app(flask_app):
    """Configure the app."""
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SESSION_COOKIE_SECURE'] = True
    flask_app.config['SECRET_KEY'] = settings.SECRET_KEY


def configure_login_manager(flask_app):
    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(flask_app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


app = create_app()
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('profile', username=current_user.username))
    else:
        return redirect(url_for('login'))
        


@app.route('/<username>')
def profile(username):
    user = user_with_username(username)
    if user is None:
        response = """
            {% extends "base.html" %}
            {% block content %}
            <h1 class="title">
                User {username} does not exist
            </h1>
            {% endblock %}
        """
        return render_template(response, username), 404
    else:
        avatar = hashlib.md5(username.encode('utf8')).hexdigest()
        can_edit = current_user.is_authenticated and username == current_user.username
        return render_template('profile.html', user=user, avatar=avatar, can_edit=can_edit)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(request.form)
    if request.method == 'POST':
        file = request.files['avatar']
        if file.content_type in settings.IMAGE_CONTENT_TYPES:
            avatar_filename = hashlib.md5(current_user.username.encode('utf8')).hexdigest()
            path = os.path.join(app.instance_path,
                                settings.UPLOADS_FOLDER, avatar_filename)
            file.save(path)
        return redirect(url_for('profile', username=current_user.username))
    return render_template('edit_profile.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = request.form.get('username')
        password = request.form.get('password')
        user = user_with_username(username)
        if user and user.check_password(password):
            login_user(user, remember=True)
            return redirect(url_for('profile', username=username))
        else:
            flash('Please check your login details and try again.')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)


@app.route('/username/<username>')
def username(username):
    return json.dumps({'available': is_username_available(username), 'username': username})


@app.route('/avatar/<path:avatar>')
def avatar(avatar):
    default_path = os.path.join(app.root_path, settings.RESOURCES_FOLDER, 'rick.png')
    avatar_path = os.path.join(
        app.instance_path, settings.UPLOADS_FOLDER, avatar)
    path = avatar_path if os.path.isfile(avatar_path) else default_path
    return send_file(path, as_attachment=True, cache_timeout=-1)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
