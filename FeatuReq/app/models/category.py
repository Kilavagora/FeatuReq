from ._base import Model
from . import db

class Category(Model):
    """This class represents the category table."""
    __tablename__ = 'categories'

    name = db.Column(db.String(255))
    features = db.relationship(
        'Feature', order_by='Feature.id', cascade="all, delete-orphan")

    def __init__(self, name):
        """initialize with name."""
        self.name = name
