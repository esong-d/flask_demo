from flask import Flask
from flask_sqlalchemy import SQLAlchemy



def init_db(app: Flask, db: SQLAlchemy):
    from app.models.users import User

    with app.app_context():
        db.init_app(app)
        db.create_all()