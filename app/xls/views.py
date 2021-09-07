from flask import Blueprint, send_from_directory

from config import basedir
from models.users import Users
from utils import handle
from utils.xlstool import XLSWriter


xls = Blueprint('xls', __name__)


@xls.route('/')
def endpoint():
    data = 'endpoint is %s' % '/xls/'
    return handle.handle_success(data=data)


@xls.route('/get/user/export')
def get_user_export():
    query = Users.query.all()
    json_list = []
    for i in query:
        json_list.append(i.to_json())
    xls = XLSWriter(sheet_name='user', file_name='user_test')
    xls.export(json_list=json_list)
    return send_from_directory(basedir, 'user_test.xls', as_attachment=True)
