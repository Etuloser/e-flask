import unittest

from config import create_app, db
from utils.pdbc import PDBC
from models.user import User


class PDBCTest(unittest.TestCase):
    pdbc = PDBC()

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_setup(self):
       db.create_all()

    def test_add(self):
        o = self.pdbc.add()
        print(o)

    def test_query(self):

        o = self.pdbc.query()
        print(o)
