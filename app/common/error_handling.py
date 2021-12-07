"""Manejador base de errores"""


class AppErrorBaseClass(Exception):
    """Manejador base de errores para aplicaciones"""
    pass


class ObjectNotFound(AppErrorBaseClass):
    """Manejador base de errores para objetos"""
    pass
