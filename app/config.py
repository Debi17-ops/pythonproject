import os

# initializing the base directory path
basedir = os.path.abspath(os.path.dirname(__file__))

# defining the class config
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # setting up the database URI
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','sqlite:///employees.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False