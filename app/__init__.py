import logging

from flask import Flask
from app.models import *

# Import extensions
from .extensions import bcrypt, cors, db, jwt, ma

from config import Config



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    logging.basicConfig(level=logging.DEBUG)
    # Register blueprints
    from .api import api_bp

    app.register_blueprint(api_bp, url_prefix="/")

    return app


def register_extensions(app):
    # Registers flask extensions
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)


