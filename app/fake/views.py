from flask import Blueprint
from utils import handle
from config import db
# from models.users import Users

fake = Blueprint('fake', __name__)


@fake.route('/')
def endpoint():
    data = 'endpoint is %s' % '/fake/'
    return handle.handle_success(data=data)


# @fake.route('/get/user')
# def get_mock_data():
#     data = []
#     query = db.session.query(Users).all()
#     for i in query:
#         data.append(i.to_json())
#     return handle.handle_success(data=data)


# @fake.route('/update/user')
# def update_mock_data():
#     o = db.session.query(Users).filter(Users.username == '刘秀珍').first()
#     o.username = '刘秀'
#     db.session.commit()
#     return handle.handle_success('success')
