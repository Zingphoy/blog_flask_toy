# encoding:utf-8

import contextlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils import logger

engine = create_engine('sqlite:///flask_blog.db', echo=True)
session_factory = sessionmaker(bind=engine)


@contextlib.contextmanager
def open_session():
    session = session_factory()
    try:
        yield session
    except Exception as e:
        logger.warning(f'error while commit: {e}')
        session.rollback()
    finally:
        session.close()
