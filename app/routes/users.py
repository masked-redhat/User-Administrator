from flask import Blueprint, request
from app.services.user_service import UserService, NoUserError, InvalidIdError
from app.utils.request import ReqBody
from app.utils.response import SendResponse
from mongoengine import ValidationError
from email_validator import validate_email, EmailNotValidError

users_blueprint = Blueprint('users_blueprint', __name__)

user_fields = ['name', 'email', 'password']


@users_blueprint.route("/", methods=['GET'])
def get_users():
    users = UserService.get_users()

    # convert the users from 'User object' type to a dict
    users = list(map(lambda user: ReqBody.convert(
        user, user_fields+["id"]), users))

    return SendResponse.ok("Got users for you", {'users': users})


@users_blueprint.route("/<string:id>", methods=['GET'])
def get_user(id: str):
    try:
        user = UserService.get_user_by_id(id)
        user = ReqBody.convert(user, user_fields)  # convert user to dict
        return SendResponse.ok(f'User {id}', {'user': user})

    except NoUserError:  # when no user found
        return SendResponse.bad("Invalid Id, no user found")

    except InvalidIdError:
        return SendResponse.bad("Invalid Id, please check again")

    except Exception as e:
        print(e)
        return SendResponse.server_error()


@users_blueprint.route("/", methods=['POST'])
def create_user():
    try:
        data = ReqBody(request.get_json(), user_fields)
        if (data.some_none() == True):  # any field missing or value not given
            return SendResponse.bad("Some fields not given")

        # validate email or raise exception
        validate_email(data.get('email'))

        id = UserService.create_user(data.values)
        return SendResponse.created("User created", {'id': id})

    except ValidationError as e:
        return SendResponse.bad("Invalid values")

    except EmailNotValidError:
        return SendResponse.bad("Invalid email")

    except Exception as e:
        if (str(e).find("duplicate") != -1):
            # only email is unique, so easy to do here
            return SendResponse.bad("Email is already used", 409)

        print(e)
        return SendResponse.server_error()


@users_blueprint.route("/<string:id>", methods=['PUT'])
def update_user(id: str):
    try:
        data = ReqBody(request.get_json(), user_fields)
        user = UserService.update_user(id, data.values)  # update user

        if data.has('email'):
            validate_email(data.get('email'))

        # updated user with 'id' field
        user = ReqBody.convert(user, [*user_fields, 'id'])
        return SendResponse.ok("User updated", {'user': user})  # w/ new values

    except ValidationError as e:
        return SendResponse.bad("Invalid values")

    except InvalidIdError:
        return SendResponse.bad("Invalid Id, please check again")

    except EmailNotValidError:
        return SendResponse.bad("Invalid email")

    except NoUserError:  # when no user found
        return SendResponse.bad("Invalid Id, no user found")

    except Exception as e:
        print(e)
        return SendResponse.server_error()


@users_blueprint.route("/<string:id>", methods=['DELETE'])
def delete_user(id: str):
    try:
        UserService.delete_user(id)
        return SendResponse.no_content()

    except NoUserError:  # when no user found
        return SendResponse.bad("Invalid Id, no user found")

    except InvalidIdError:
        return SendResponse.bad("Invalid Id, please check again")

    except Exception as e:
        print(e)
        return SendResponse.server_error()
