# encoding:utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///flask_blog.db', echo=True)
Session = sessionmaker(bind=engine)
