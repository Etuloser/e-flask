import os
from config import db
from utils import handle
from utils.fake import Faker


def make_10_mock_data():
    from models.user import User

    dev_sqlite_file = os.path.join(os.path.dirname(__file__), 'data-dev.sqlite')
    if os.path.exists(dev_sqlite_file):
        fake = Faker()
        for _ in range(10):
            o = User(fake.name(), fake.email())
            db.session.add(o)
        db.session.commit()
        return handle.handle_success()
    else:
        db.create_all()
        return handle.handle_error(data='setup env, please try again')
