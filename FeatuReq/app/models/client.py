"""Client model"""
from ._base import Model
from . import db


class Client(Model):
    """This class represents the client table."""
    __tablename__ = 'clients'

    name = db.Column(db.String(255))
    features = db.relationship(
        'Feature', order_by='Feature.id', cascade="all, delete-orphan")

    def __init__(self, name):
        """initialize with name."""
        self.name = name
