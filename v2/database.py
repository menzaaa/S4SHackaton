
from sqlalchemy.orm import relationship

from .extentions import db

relationship = relationship

class CRUDMixin(object):

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        # Dont change the ID
        kwargs.pop('id', None)
        for attr, value in kwargs.iteritems():
            if value is not None:
                setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        """Save the record"""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.sesion.delete(self)
        return commit and db.session.commit()

class Model(CRUDMixin, db.Model):
    """Base model class with CRUD methods"""
    __abstract__ = True


class SurrogatePK(object):
    
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    
    @classmethod
    def get_by_id(cls, id):
        if id <= 0:
            raise ValueError('ID must be > 0')
        if any(
            (isinstance(id, basestring) and id.isdigit(),
            isinstance(id, (int, float))),
        ):
            return cls.query.get(int(id))
        return None

def ReferenceCol(tablename, nullable=False, pk_name='id', **kwargs):
    """Column that adds primary key foreign key reference.

    Usage: ::

        category_id = ReferenceCol('category')
        category = relationship('Category', backref='categories')
    """
    
    return db.Column(
        db.ForeignKey("{0}.{1}".format(tablename, pk_name),
        nullable=nullable, **kwargs) # pragma: no cover
    )