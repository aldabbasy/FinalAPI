"""Data models."""
from wsgi import db
from Utils import dump_datetime

class User(db.Model):
    """Data model for user accounts."""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    password = db.Column(db.String(200), index=False, unique=False, nullable=False)
    createdBy = db.Column(db.String(200), index=False, unique=False, nullable=False)
    createdAt = db.Column(db.DateTime, index=False, unique=False, nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        created_by = User.query.filter_by(id=int(self.createdBy)).first()
        created_by_name = ''
        if created_by:
            created_by_name = created_by.username
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'createdBy': {'id': self.createdBy, 'username': created_by_name},
            'createdAt': dump_datetime(self.createdAt)
            # This is an example how to deal with Many2Many relations
        }

    def __repr__(self):
        return "<User {}>".format(self.username)