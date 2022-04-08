# SQLAlchemy settings
DATABASE = "db.sqlite"
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+DATABASE
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Other settings
UPLOADS_FOLDER = 'uploads'
RESOURCES_FOLDER = 'resources'
SECRET_KEY="somethingunique"
IMAGE_CONTENT_TYPES = tuple('image/gif image/bmp image/jpeg image/png image/svg+xml image/tiff image/webp'.split())