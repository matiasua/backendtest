import datetime
import marshmallow
from flask import request, jsonify, Blueprint, current_app
from project import db, bcrypt
from project.models import Grupos, Usuario
from project.schemas import grupo_schema

blueprint = Blueprint('grupo', __name__)

@blueprint.route('/create_group', methods=['POST'])
def create():
  # Validar que exista usuario autenticado que esta creando el grupo
  # Obtener los datos del usuario autenticado (especialmente id)
  user = Usuario.query.get_or_404(1)
  data = grupo_schema.load(request.get_json())
  data.users = [user]
  db.session.add(data)
  db.session.commit()

  return grupo_schema.dump(data), 201


@blueprint.route('/groups', methods=['GET'])
def list():
  group = Grupos.query.all()

  return jsonify(grupo_schema.dump(group, many=True)), 200

  # @blueprint.route('/add_user', methods=['POST'])
  # def add():
  #   user = 
