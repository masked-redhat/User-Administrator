from flask import Blueprint, request
from app.services.user_service import UserService, NoUserError
from app.utils.request import ReqBody
from app.utils.response import SendResponse
from mongoengine import ValidationError

users_blueprint = Blueprint('users_blueprint', __name__)

users_fields = ['name', 'email', 'password']


@users_blueprint.route("/", methods=['GET'])
def get_users():
    users = UserService.get_users()

    # convert the users from 'User object' type to a dict
    users = list(map(lambda user: ReqBody.convert(
        user, users_fields+["id"]), users))

    return SendResponse.ok("Got users for you", {'users': users})


@users_blueprint.route("/<string:id>", methods=['GET'])
def get_user(id: str):
    try:
        user = UserService.get_user_by_id(id)
        user = ReqBody.convert(user, users_fields)  # convert user to dict
        return SendResponse.ok(f'User {id}', {'user': user})

    except NoUserError:  # when no user found
        return SendResponse.bad("Invalid Id, no user found")

    except:
        return SendResponse.server_error()


@users_blueprint.route("/", methods=['POST'])
def create_user():
    try:
        data = ReqBody(request.get_json(), users_fields)
        if (data.some_none() == True):  # any field missing or value not given
            return SendResponse.bad("Some fields not given")

        id = UserService.create_user(data.values)
        return SendResponse.created("User created", {'id': id})

    except ValidationError as e:
        return SendResponse.bad("Invalid values")

    except Exception as e:
        if (str(e).find("duplicate") != -1):
            # only email is unique, so easy to do here
            return SendResponse.bad("Email is already used", 409)

        return SendResponse.server_error()


@users_blueprint.route("/<string:id>", methods=['PUT'])
def update_user(id: str):
    try:
        data = ReqBody.convert(request.get_json(), users_fields)
        user = UserService.update_user(id, data)  # update user

        # updated user with 'id' field
        user = ReqBody.convert(user, [*users_fields, 'id'])
        return SendResponse.ok("User updated", {'user': user})  # w/ new values

    except ValidationError as e:
        return SendResponse.bad("Invalid values")

    except NoUserError:  # when no user found
        return SendResponse.bad("Invalid Id, no user found")

    except:
        return SendResponse.server_error()


@users_blueprint.route("/<string:id>", methods=['DELETE'])
def delete_user(id: str):
    try:
        UserService.delete_user(id)
        return SendResponse.no_content()

    except NoUserError:  # when no user found
        return SendResponse.bad("Invalid Id, no user found")

    except:
        return SendResponse.server_error()
