from flask import Blueprint
from utils import handle
from utils.command import Command

command = Blueprint('command', __name__)


@command.route('/')
def endpoint():
    data = 'endpoint is %s' % '/command/'
    return handle.handle_success(data=data)


@command.route('/health/check')
def health_check():
    cmd = 'ls /opt'
    data = Command().get_status_output(cmd)
    return handle.handle_success(str(data))
