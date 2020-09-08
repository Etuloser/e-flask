from config import db
from models.user import User


class PDBC():
    def __init__(self):
        pass

    def setup(self):
        db.create_all()

    def add(self):
        admin = User('admin', 'admin@example.com')
        db.session.add(admin)
        db.session.commit()

    def query(self):
        result = User.query.all()
        print(result)
