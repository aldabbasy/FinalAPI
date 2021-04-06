from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT

db = SQLAlchemy()

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    db.init_app(app)

    with app.app_context():
        from .Controllers import usersController  # Import routes
        app.register_blueprint(usersController, url_prefix='/api/users')
        db.create_all()  # Create database tables for our data models
        #import auth config
        from .Utils.auth import authenticate, identity
        jwt = JWT(app, authenticate, identity)
        
        return app