# encoding:utf-8
import contextlib

import contextlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

from utils import logger

__engine = create_engine('sqlite:///database/flask_blog.db', echo=True)
__session_factory = sessionmaker(bind=__engine)


@contextlib.contextmanager
def get_session():
    session = __session_factory()
    try:
        yield session
    except OperationalError as e:   # 注：在这里即使return 500也没有效果
        session.rollback()
        logger.error(f'error occurs in sqlalchemy session: {e}')
        raise e
    finally:
        session.close()
