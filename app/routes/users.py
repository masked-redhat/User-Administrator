from flask import Blueprint, request
from app.services.user_service import UserService
from app.utils.request import ReqBody

users_blueprint = Blueprint('users_blueprint', __name__)

users_fields = ['name', 'email', 'password']


@users_blueprint.route("/", methods=['GET'])
def get_users():
    users = UserService.get_users()

    _users = []
    for user in users:
        _users.append(ReqBody(user, users_fields+["id"]).values)

    return _users


@users_blueprint.route("/<id>", methods=['GET'])
def get_user(id):
    user = UserService.get_user_by_id(id)

    return ReqBody(user, users_fields+["id"]).values


@users_blueprint.route("/", methods=['POST'])
def create_user():
    data = ReqBody(request.get_json(), users_fields)
    if (data.some_none() == True):
        return "Some fields not given"
    id = UserService.create_user(data.values)
    return {
        'id': id
    }


@users_blueprint.route("/<id>", methods=['PUT'])
def update_user(id):
    data = ReqBody(request.get_json(), users_fields)
    user = UserService.update_user(id, data.values)
    return ReqBody(user, users_fields+['id']).values


@users_blueprint.route("/<id>", methods=['DELETE'])
def delete_user(id):
    UserService.delete_user(id)
    return "Deleted"
