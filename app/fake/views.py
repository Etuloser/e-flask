import os
from flask import Blueprint

from config import db, basedir
from models.users import Users
from utils import handle
from utils.fake import Fake

fake = Blueprint('fake', __name__)


@fake.route('/')
def endpoint():
    data = 'endpoint is %s' % '/fake/'
    return handle.handle_success(data=data)


@fake.route('/get/user')
def get_mock_data():
    data = []
    query = db.session.query(Users).all()
    for i in query:
        data.append(i.to_json())
    return handle.handle_success(data=data)


@fake.route('/update/user')
def update_mock_data():
    o = db.session.query(Users).filter(Users.username == '刘秀珍').first()
    o.username = '刘秀'
    db.session.commit()
    return handle.handle_success('success')


@fake.route("/user")
def fake_user():
    from models.users import Users

    dev_sqlite_file = os.path.join(basedir, 'data-dev.sqlite')
    if os.path.exists(dev_sqlite_file):
        fake = Fake().fake
        for _ in range(10):
            o = Users(username=fake.name(), email=fake.email())
            db.session.add(o)
        db.session.commit()
        return handle.handle_success()
    else:
        db.create_all()
        return handle.handle_error(data='setup env, please try again')
