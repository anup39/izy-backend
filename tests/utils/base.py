import unittest
from app import db, create_app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy_session import flask_scoped_session
from config import Config
import os


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        flask_scoped_session(sessionmaker(bind=create_engine(f"{Config.DB_DIALECT}://{Config.DB_USERNAME}:{Config.DB_PASSWORD}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}", pool_size=5), autocommit=False, autoflush=False), self.app)
        self.app_context.push()
        self.client = self.app.test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        self.app_context.pop()
