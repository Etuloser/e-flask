import os
import re
import pymysql
from config import config

flask_config = os.getenv('FLASK_CONFIG') or 'default'
db_uri = config[flask_config].SQLALCHEMY_DATABASE_URI

o = re.search(r'mysql://([^:]):(.*)@(.*):(\d+)/([^?])', db_uri)
user = o.group(1)
passwd = o.group(2)
host = o.group(3)
port = o.group(4)
db = o.group(5)


class PDBC:
    """
    Use pymysql operate database
    """

    def __init__(self):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port = port

        self.conn = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.passwd,
            database=self.db,
            port=int(self.port)
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def close(self):
        self.cursor.close()
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def sql_execute(self, sql):
        """
        :param sql:
        :return:
        """
        self.cursor.execute(sql)
        return self.cursor
