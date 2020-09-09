from flask import Blueprint
from utils import handle
from config import db
from models.user import User

fake = Blueprint('fake', __name__)


@fake.route('/')
def endpoint():
    data = 'endpoint is %s' % '/fake/'
    return handle.handle_success(data=data)


@fake.route('/get/user')
def get_mock_data():
    data = []
    query = db.session.query(User).all()
    for i in query:
        data.append(i.to_json())
    return handle.handle_success(data=data)
