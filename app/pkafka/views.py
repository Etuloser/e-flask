from flask import Blueprint
from utils import handle
from utils.pkafka import Pkafka

pkafka = Blueprint('pkafka', __name__)


@pkafka.route('/')
def endpoint():
    data = 'endpoint is %s' % '/pkafka/'
    return handle.handle_success(data=data)


@pkafka.route('/health/check')
def health_check():
    version = Pkafka().check_version()
    print(version)
    data = {
        'version': version
    }
    return handle.handle_error(data=str(data))
