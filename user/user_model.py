# -*- coding: utf-8 -*-

"""
blog_flask_toy/server/user.user_model
~~~~~~~~~~~~~~~

"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from database import __engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, autoincrement=True)
    email = Column(String(64), nullable=True, primary_key=True)
    username = Column(String(64), nullable=False, index=True, unique=True)
    password = Column(String(16), nullable=False)

    def repr(self):
        return f'User information: {self.id} - {self.name} - {self.email}'


Base.metadata.create_all(__engine)
