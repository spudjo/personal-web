# coding=utf-8

from sqlalchemy import Column, String

from .database import Entity, Base


class Guestbook(Entity, Base):
    __tablename__ = 'guestbook'

    name = Column(String)
    message = Column(String)

    def __init__(self, name, message, created_by):
        Entity.__init__(self, created_by)
        self.name = name
        self.message = message
