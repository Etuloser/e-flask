from flask import Blueprint
from utils import handle
from config import db
from models.user import User

xls = Blueprint('xls', __name__)


@xls.route('/')
def endpoint():
    data = 'endpoint is %s' % '/xls/'
    return handle.handle_success(data=data)


@xls.route('/get/user/export')
def get_user_export():
    from app.fake.views import get_mock_data
    data = get_mock_data()['data']
    print(data)
    return handle.handle_success()
