from ._base import Model
from . import db


class Feature(Model):
    """This class represents the feature table."""
    __tablename__ = 'features'

    title = db.Column(db.String(255))
    description = db.Column(db.String)
    priority = db.Column(db.Integer)
    category = db.Column(db.Integer, db.ForeignKey('categories.id'))
    client = db.Column(db.Integer, db.ForeignKey('clients.id'))
    target_date = db.Column(db.DateTime)
    complete = db.Column(db.Boolean, default=False)

    def __init__(self, title, description, priority,
                 client, category, target_date, complete=False):
        """initialize with name."""
        self.title = title
        self.description = description
        self.priority = priority
        self.client = client
        self.category = category
        self.target_date = target_date
        self.complete = complete
