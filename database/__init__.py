# encoding:utf-8
import contextlib

import contextlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base

from utils import logger
from database import __engine

Base = declarative_base()
Base.metadata.create_all(__engine)

__engine = create_engine('sqlite:///database/flask_blog.db', echo=True)
__session_factory = sessionmaker(bind=__engine)


@contextlib.contextmanager
def get_session():
    session = __session_factory()
    try:
        yield session
    except OperationalError as e:  # 注：在这里即使return 500也没有效果
        session.rollback()
        logger.error(f'error occurs in sqlalchemy session: {e}')
        raise e
    finally:
        session.close()
