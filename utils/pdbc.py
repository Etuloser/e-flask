import os

from config import config
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


def get_db_session():
    flask_config = os.getenv('FLASK_CONFIG') or 'default'
    db_uri = config[flask_config].SQLALCHEMY_DATABASE_URI
    engine = create_engine(db_uri)
    session_factory = sessionmaker(bind=engine)
    session = scoped_session(session_factory)
    return session
