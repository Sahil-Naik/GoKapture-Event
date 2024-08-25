from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/task_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = '1234'  # Change this to a random secret key

    db.init_app(app)
    JWTManager(app)
    migrate = Migrate(app, db)

    # Import the models to register them with SQLAlchemy
    # You can import models here without any issues because
    # the db object is already initialized
    from .models import User

    # Register routes
    from .routes import register_routes
    register_routes(app)

    return app
