"""Manejador base de errores"""


class AppErrorBaseClass(Exception):
    """Manejador base de errores para aplicaciones"""


class ObjectNotFound(AppErrorBaseClass):
    """Manejador base de errores para objetos"""
