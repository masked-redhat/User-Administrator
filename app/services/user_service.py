from app.models.User import User


class NoUserError(Exception):
    """Custom error when no user found"""
    pass


class InvalidIdError(Exception):
    """Custom error when no user found"""
    pass


class UserService:
    @staticmethod
    def get_users():
        users = User.objects()
        return users

    @staticmethod
    def get_user_by_id(id: str):
        if (len(id) != 24):  # simplest error checking for id
            raise InvalidIdError

        user = User.objects(id=id).first()  # id is in string

        if user is None:
            raise NoUserError

        return user

    @staticmethod
    def create_user(data: dict = {}):
        user = User(name=data['name'], email=data['email'],
                    password=data['password'])
        user.save()
        return user.id.__str__()  # gets the stringified version of the ObjectID

    @staticmethod
    def update_user(id: str, data: dict = {}):
        if (len(id) != 24):  # simplest error checking for id
            raise InvalidIdError

        user = User.objects(id=id).first()

        if user is None:
            raise NoUserError

        # set new values in the user
        for key, val in data.items():
            setattr(user, key, val)
        user.save()

        return user

    @staticmethod
    def delete_user(id: str):
        if (len(id) != 24):  # simplest error checking for id
            raise InvalidIdError

        user = User.objects(id=id).first()

        if user is None:
            raise NoUserError

        user.delete()
