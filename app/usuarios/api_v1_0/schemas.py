""" Archivo con schemas """
import re
from marshmallow import fields, validates, ValidationError
from app.ext import ma


class UsuarioSchema(ma.Schema):
    """ Schema para Usuario """
    id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True)
    email = fields.Email(
        required=True,
        error_messages={"email": "El correo no tiene formato válido."})
    clave = fields.String(required=True)

    @validates("nombre")
    def validate_nombre(self, value):
        """ Validacion para campo nombre """
        if len(value) < 3:
            raise ValidationError("El largo debe ser mayor a 3 caracteres.")

        if len(value) > 60:
            raise ValidationError("El largo debe ser menor a 60 caracteres.")

    @validates("clave")
    def validate_clave(self, value):
        """ Validacion para campo clave """
        pattern = re.search(r"\d", value)
        if not pattern:
            raise ValidationError("Debe tener al menos un dígito.")

        pattern = re.search(r"[a-z]", value)
        if not pattern:
            raise ValidationError("Debe tener una letra en minuscula.")

        pattern = re.search(r"[A-Z]", value)
        if not pattern:
            raise ValidationError("Debe tener una letra en mayúscula.")

        pattern = re.search(r"[#$%&!=\+_]+", value)
        if not pattern:
            raise ValidationError("No posee caracteres especiales (#$%&!=+_).")
