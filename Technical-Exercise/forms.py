from wtforms import Form, BooleanField, StringField, PasswordField, BooleanField, validators, ValidationError, FileField
from flask_wtf import FlaskForm
from database.users import is_username_available
import re


class RegistrationForm(Form):
    username_validators = [validators.DataRequired(), validators.Length(min=3, max=80), 
                            validators.Regexp("^[a-z0-9]+$", re.IGNORECASE, "Only use letters and numbers")]
    username = StringField('Username', username_validators)
    email = StringField('Email Address', 
                        [validators.DataRequired(), validators.Email(), validators.Length(min=6, max=120)])
    password = PasswordField('Password', [validators.DataRequired()])

    def validate_username(form, field):
        if not is_username_available(field.data):
            raise ValidationError(f"User {field.data} is not available")

class LoginForm(Form):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

class EditProfileForm(FlaskForm):
    
    avatar = FileField('Avatar')
