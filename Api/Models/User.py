"""Data models."""
from .. import db
from ..Utils import dump_datetime

class User(db.Model):
    """Data model for user accounts."""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=False, unique=True, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    createdAt = db.Column(db.DateTime, index=False, unique=False, nullable=False)

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id': self.id,
           'username': self.username,
            'email': self.email,
           'createdAt': dump_datetime(self.createdAt)
           # This is an example how to deal with Many2Many relations
       }

    def __repr__(self):
        return "<User {}>".format(self.username)