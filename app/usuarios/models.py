"""Archivo que declara Modelo"""
from app.db import db, BaseModelMixin


class Usuario(db.Model, BaseModelMixin):
    """ Modelo para Usuario """
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    clave = db.Column(db.String)

    def __init__(self, nombre, email, clave):
        self.nombre = nombre
        self.email = email
        self.clave = clave

    def __repr__(self):
        return f'Usuario({self.nombre} <{self.email}>)'

    def __str__(self):
        return f'{self.nombre} <{self.email}>'
