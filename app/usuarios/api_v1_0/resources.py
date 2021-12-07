"""Archivo que contiene los endpoints"""
from flask import request, Blueprint
from flask_restful import Api, Resource
from marshmallow import ValidationError
from app.common.error_handling import ObjectNotFound
from .schemas import UsuarioSchema
from ..models import Usuario

usuarios_v1_0_bp = Blueprint('usuarios_v1_0_bp', __name__)
usuario_schema = UsuarioSchema()
api = Api(usuarios_v1_0_bp)

class UsuarioResource(Resource):
    """Permite administrar un usuario"""


    def delete(self, email):
        """Permite eliminar un usuario"""
        usuario = Usuario.simple_filter_one(email=email)
        if usuario is None:
            raise ObjectNotFound('El usuario no existe')

        usuario.delete()
        return '', 204

api.add_resource(
    UsuarioResource,
    '/api/v1.0/usuarios/<string:email>',
    endpoint='usuario_resource')
