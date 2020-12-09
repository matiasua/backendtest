from marshmallow import fields
from project import ma
from project.models import Usuario, Grupos


class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    # grupo = fields.Nested(nested='GruposSchema', many=True)
    class Meta:
        model = Usuario
        load_instance = True
        load_only = ('password', )


usuario_schema = UsuarioSchema()


class GruposSchema(ma.SQLAlchemyAutoSchema):
    # user_id = fields.Int()
    class Meta:
        model = Grupos
        load_instance = True

grupo_schema = GruposSchema()