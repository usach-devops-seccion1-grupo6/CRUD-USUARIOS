"""Archivo que contiene los endpoints"""
import datetime
from flask import request, Blueprint
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from marshmallow import ValidationError
from app.common.error_handling import ObjectNotFound
from .schemas import UsuarioSchema
from ..models import Usuario

usuarios_v1_0_bp = Blueprint('usuarios_v1_0_bp', __name__)
usuario_schema = UsuarioSchema()
api = Api(usuarios_v1_0_bp)


class UsuarioAuthResource(Resource):
    """Permite autentificacion de usuarios."""

    def post(self):
        """Entrega un json token"""
        temp = request.get_json()

        usuario = Usuario.simple_filter_one(email=temp['email'])
        if not usuario:
            return {'msg': 'El correo o clave invalidos'}, 404

        autorizado = usuario.check_clave(temp['clave'])
        if not autorizado:
            return {'msg': 'El correo o clave invalidos'}, 404

        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(usuario.id), expires_delta=expires)
        return {'token': access_token}, 200


class UsuarioListResource(Resource):
    """Maneja los acciones para listar y agregar usuarios."""

    @jwt_required()
    def get(self):
        """Permite listar un usuario"""
        usuarios = Usuario.get_all()
        result = usuario_schema.dump(usuarios, many=True)
        return result

    def post(self):
        """Permite agregar un usuario"""
        temp = request.get_json()
        try:
            data = usuario_schema.load(temp)

            usuario = Usuario.simple_filter_one(email=data['email'])
            if usuario:
                return {'msg': 'El usuario ya existe'}, 404

        except ValidationError as err:
            raise ObjectNotFound(err.messages) from err

        usuario = Usuario(
            nombre=data['nombre'],
            email=data['email'],
            clave=data['clave']
        )

        usuario.hash_clave()
        usuario.save()
        resp = usuario_schema.dump(usuario)
        return resp, 201


class UsuarioResource(Resource):
    """Permite agregar un usuario"""

    @jwt_required()
    def get(self, email):
        """Permite mostrar un usuario"""
        usuario = Usuario.simple_filter_one(email=email)
        if usuario is None:
            return {'msg': 'El usuario no existe'}, 404

        resp = usuario_schema.dump(usuario)
        return resp

    @jwt_required()
    def delete(self, email):
        """Permite eliminar un usuario"""
        usuario = Usuario.simple_filter_one(email=email)
        if usuario is None:
            return {'msg': 'El usuario no existe'}, 404

        usuario_id = int(get_jwt_identity())
        if usuario.id != usuario_id:
            return {'msg': 'Usuario distinto'}, 500

        usuario.delete()
        return '', 204

    @jwt_required()
    def put(self, email):
        """Permite modificar los datos de mi propio usuario"""
        temp = request.get_json()
        try:
            temp['email'] = email
            data = usuario_schema.load(temp)

            usuario = Usuario.simple_filter_one(email=email)
            if usuario is None:
                return {'msg': 'El usuario no existe'}, 404

            usuario_id = int(get_jwt_identity())
            if usuario.id != usuario_id:
                return {'msg': 'Usuario distinto'}, 500

        except ValidationError as err:
            raise ObjectNotFound(err.messages) from err

        usuario.nombre = data['nombre']
        usuario.clave = data['clave']

        usuario.hash_clave()
        usuario.update()
        return {'msg': 'Actualizado'}, 200


api.add_resource(
    UsuarioListResource,
    '/api/v1.0/usuarios/',
    endpoint='usuario_list_resource')

api.add_resource(
    UsuarioResource,
    '/api/v1.0/usuarios/<string:email>',
    endpoint='usuario_resource')

api.add_resource(
    UsuarioAuthResource,
    '/api/v1.0/usuarios/auth/',
    endpoint='usuario_auth_resource')
