"""Class-based Flask app configuration."""
from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Configuration from environment variables."""

    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_ENV = environ.get("FLASK_DEBUG")
    FLASK_APP = "wsgi.py"
    CSRF_ENABLED = os.environ.get("CSRF_ENABLED")

    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"

    # API
    BEST_BUY_API_KEY = environ.get("BEST_BUY_API_KEY")
    
    #DB
    SQLALCHEMY_ECHO = SQLALCHEMY_ECHO = os.environ.get('SQLALCHEMY_ECHO') in ('1', 'True')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = os.environ.get("SQLALCHEMY_COMMIT_ON_TEARDOWN")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
