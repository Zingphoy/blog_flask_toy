# -*- coding: utf-8 -*-

"""
blog_flask_toy/server/user.user_model
~~~~~~~~~~~~~~~

"""

from sqlalchemy import Column, Integer, String

from database import Base


class User(Base):
    __tablename__ = 'user'

    # id = Column(Integer, autoincrement=600, primary_key=True)
    id = Column(Integer, primary_key=True)  # sqlite底层实现特殊，不需要id自增写法
    email = Column(String(64), nullable=True, index=True, unique=True)
    username = Column(String(64), nullable=False, index=True, unique=True)
    password = Column(String(16), nullable=False)

    def repr(self):
        return f'User information: {self.id} - {self.name} - {self.email}'
