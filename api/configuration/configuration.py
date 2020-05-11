from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os


class Configuration:
    _app = None
    _db = None

    def __init__(self):
        raise RuntimeError('Cannot instantiate Configuration class.')

    @classmethod
    def initialize_app(cls):
        cls.get_app()
        cls.get_db()

    @classmethod
    def get_app(cls):
        if cls._app is None:
            cls._app = Flask(__name__)
            basedir = os.path.abspath(os.path.dirname(__file__))
            cls._app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
            cls._app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        return cls._app

    @classmethod
    def get_db(cls):
        if cls._db is None:
            cls._db = SQLAlchemy(cls.get_app())
        return cls._db
