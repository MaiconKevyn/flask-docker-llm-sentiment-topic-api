"""This module initializes the Flask application and its configurations."""

# Standard library imports
import os
import logging

# Third party imports
from flask import Flask

# Local application imports
from .routes import bp as main_blueprint

def configure_logging():
    """
    Configures the logging for the application.
    Sets the logging level to INFO and specifies the log format.
    """
    format_str = '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    logging.basicConfig(level=logging.INFO, format=format_str)

def create_app():
    """
    Creates and configures an instance of a Flask application.
    Returns the configured Flask application instance.
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'you-will-never-guess')
    app.config['DEBUG'] = True

    configure_logging() #chama a funcao para configurar o log

    app.register_blueprint(main_blueprint, url_prefix='/')

    return app
