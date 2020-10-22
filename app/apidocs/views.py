from flask import Blueprint
from utils import handle

apidocs = Blueprint('apidocs', __name__)


@apidocs.route('/')
def endpoint():
    data = 'endpoint is %s' % '/apidocs/'
    return handle.handle_success(data=data)


@apidocs.route('/list')
def get_list():
    from manage import app
    result = app.url_map
    data = result
    return handle.handle_error(str(data))
