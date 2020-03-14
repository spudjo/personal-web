# coding=utf-8

from sqlalchemy import Column, String

from .database import Entity, Base

from marshmallow import Schema, fields


class Guestbook(Entity, Base):
    __tablename__ = 'guestbook'

    name = Column(String)
    message = Column(String)

    def __init__(self, name, message, created_by):
        Entity.__init__(self, created_by)
        self.name = name
        self.message = message


class GuestbookSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    message = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
