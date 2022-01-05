import os

from flask import Flask
from flask_apscheduler import APScheduler
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SCHEDULER_API_ENABLED = True
    KAFKA_URI = os.environ.get('KAFKA_URI')
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}

db = SQLAlchemy()
scheduler = APScheduler()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    scheduler.init_app(app)
    # 注意,在Debug模式开启的情况下,scheduler的task会执行两次
    # scheduler.start()

    from app.fake.views import fake as fake_blueprint
    app.register_blueprint(fake_blueprint, url_prefix='/fake')

    from app.xls.views import xls as xls_blueprint
    app.register_blueprint(xls_blueprint, url_prefix='/xls')

    from app.pdbc.views import pdbc as xls_blueprint
    app.register_blueprint(xls_blueprint, url_prefix='/pdbc')

    from app.apidocs.views import apidocs as apidocs_blueprint
    app.register_blueprint(apidocs_blueprint, url_prefix='/apidocs')

    from app.pkafka.views import pkafka as pkafka_blueprint
    app.register_blueprint(pkafka_blueprint, url_prefix='/pkafka')

    from app.command.views import command as command_blueprint
    app.register_blueprint(command_blueprint, url_prefix='/command')

    return app


def create_api(app):
    api = Api(app)

    from app.user.views import User, UserList
    api.add_resource(UserList, '/user')
    api.add_resource(User, '/user/<user_id>')
    return api
