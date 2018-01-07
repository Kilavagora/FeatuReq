from abc import ABCMeta, abstractmethod
from . import db


class Model(db.Model):
    """Base model to be inherited in all models."""
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    @abstractmethod
    def save(self):
        """Save model to DB"""
        db.session.add(self)
        db.session.commit()

    @classmethod
    @abstractmethod
    def get_all(cls):
        """Gell all items"""
        return cls.query.all()

    @abstractmethod
    def delete(self):
        """Delete the record from DB"""
        db.session.delete(self)
        db.session.commit()

    @abstractmethod
    def __repr__(self):
        return "<{0}: {1}>".format(self.__class__.__name__, self.id)

    @abstractmethod
    def to_dict(self):
        # return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        return {k.name: getattr(self, k.name) for k in self.__table__.columns}
