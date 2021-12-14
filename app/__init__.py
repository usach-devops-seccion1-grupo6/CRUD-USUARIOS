"""Archivo que contiene el lanzador de Flask"""
import os
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from app.common.error_handling import ObjectNotFound, AppErrorBaseClass
from app.db import db
from app.usuarios.api_v1_0.resources import usuarios_v1_0_bp
from .ext import ma, migrate


def create_app():
    """Funcion que lanza la aplicación"""
    app = Flask(
        __name__,
        instance_relative_config=True)

    app_settings = 'app.config.Production'
    if 'APP_SETTINGS' in dict(os.environ):
        app_settings = os.environ['APP_SETTINGS']

    app.config.from_object(app_settings)

    # Inicializa las extensiones
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # Captura todos los errores 404
    Api(app, catch_all_404s=True)
    Bcrypt(app)
    JWTManager(app)

    # Deshabilita el modo estricto de acabado de una URL con /
    app.url_map.strict_slashes = False

    # Registra los blueprints
    app.register_blueprint(usuarios_v1_0_bp)

    # Registra manejadores de errores personalizados
    register_error_handlers(app)
    return app


def register_error_handlers(app):
    """Administrador de errores"""

    @app.errorhandler(Exception)
    def handle_exception_error(error):
        msg = str(error) if app.debug else 'Internal server error'
        return jsonify({'msg': msg}), 500

    @app.errorhandler(405)
    def handle_405_error(error):
        msg = str(error) if app.debug else 'Method not allowed'
        return jsonify({'msg': msg}), 405

    @app.errorhandler(403)
    def handle_403_error(error):
        msg = str(error) if app.debug else 'Forbidden error'
        return jsonify({'msg': msg}), 403

    @app.errorhandler(404)
    def handle_404_error(error):
        msg = str(error) if app.debug else 'Not Found error'
        return jsonify({'msg': msg}), 404

    @app.errorhandler(AppErrorBaseClass)
    def handle_app_base_error(error):
        return jsonify({'msg': str(error)}), 500

    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found_error(error):
        return jsonify({'msg': str(error)}), 404
