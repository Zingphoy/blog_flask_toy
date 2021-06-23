# encoding:utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///flask_blog.db', echo=True)
session_factory = sessionmaker(bind=engine)

