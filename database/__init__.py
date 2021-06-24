# encoding:utf-8
import contextlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils import logger

__engine = create_engine('sqlite:///flask_blog.db', echo=True)
__session_factory = sessionmaker(bind=__engine)


@contextlib.contextmanager
def get_session():
    session = __session_factory()
    try:
        yield session
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
