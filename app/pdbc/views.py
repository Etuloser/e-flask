import os
from flask import Blueprint
from utils import handle
from utils.pdbc import PDBC

pdbc = Blueprint('pdbc', __name__)


@pdbc.route('/')
def endpoint():
    data = 'endpoint is %s' % '/pdbc/'
    return handle.handle_success(data=data)


@pdbc.route('/health/check')
def health_check():
    try:
        with PDBC() as conn:
            sql = 'SELECT VERSION()'
            data = conn.sql_execute(sql).fetchone()
            return handle.handle_success(data)
    except Exception as e:
        data = {
            'err_msg': str(e),
            'mysql_host': os.getenv('PYMYSQL_HOST') or None,
            'mysql_port': os.getenv('PYMYSQL_PORT') or None,
            'mysql_db': os.getenv('PYMYSQL_DB') or None
        }
        return handle.handle_error(data)
