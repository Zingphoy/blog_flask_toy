# -*- coding: utf-8 -*-

"""
blog_flask_toy/server/user.user_model
~~~~~~~~~~~~~~~

"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(64), nullable=True)
    username = Column(String(64), nullable=False, index=True, unique=True)
    password = Column(String(16), nullable=False)

    def repr(self):
        return f'User information: {self.id} - {self.name} - {self.email}'

# Base.metadata.create_all(engine)
