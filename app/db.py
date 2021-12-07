"""Archivo que gestion conexion a base de dato"""
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class BaseModelMixin:
    """Clase base para ORM"""

    def save(self):
        """Permite guardar un objeto"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Permite borrar un objeto"""
        db.session.delete(self)
        db.session.commit()

    def update(self):
        """Permite updatear un objeto"""
        db.session.commit()

    @classmethod
    def get_all(cls):
        """Obtiene todos los registros"""
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        """Obtiene un registro en base al ID"""
        return cls.query.get(id)

    @classmethod
    def simple_filter_one(cls, **kwargs):
        """Obtiene el primer registro filtrado"""
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def simple_filter(cls, **kwargs):
        """Obtiene todos los registro filtrados"""
        return cls.query.filter_by(**kwargs).all()
