import unittest

from flask import current_app

from config import create_app, db


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_env_load(self):
        import os

        self.assertIsNone(os.getenv('DATABASE_URL'))

        from dotenv import load_dotenv
        dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)

        self.assertIsNotNone(os.getenv('DATABASE_URL'))

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
