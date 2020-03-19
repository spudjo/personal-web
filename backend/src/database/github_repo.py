# coding=utf-8

from sqlalchemy import Column, String, Integer, DateTime
from .database import Entity, Base
from marshmallow import Schema, fields


class GithubRepo(Base):
    __tablename__ = 'github_repo'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    url = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self, id, name, description, url, created_at, updated_at):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.created_at = created_at
        self.updated_at = updated_at


class GithubRepoSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    description = fields.Str()
    url = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()