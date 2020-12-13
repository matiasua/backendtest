from functools import wraps
from flask import request, jsonify, Blueprint
from project import db
from project.models import Aparatos
from project.schemas import aparatos_schema
from project.endpoints.users import autenticar

blueprint = Blueprint('aparatos', __name__)


@blueprint.route ('/register_aparatos', methods=['GET'])
@autenticar
def list(usuario):
    aparatos = Aparatos.query.all()
    print(aparatos)

    return jsonify(producto_schema.dump(aparatos, many=True)), 200 


@blueprint.route('/register_aparatos', methods=['POST'])
@autenticar
def regis(usuario):

    aparatos = aparatos_schema.load(request.json)

    db.session.add(aparatos)
    db.session.commit()

    return producto_schema.dump(aparatos),201