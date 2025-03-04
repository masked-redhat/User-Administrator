from app.models.User import User


class UserService:
    @staticmethod
    def get_users():
        users = User.objects()
        return users

    @staticmethod
    def get_user_by_id(id):
        if (type(id) != 'string'):
            raise TypeError(f"Invalid id : ${id}")

        user = User.objects(id=id).first()
        if (user == None):
            raise AttributeError(f"No user found with id ${id}")

        return user

    @staticmethod
    def create_user(data):
        user = User(name=data['name'], email=data['email'],
                    password=data['password'])
        user.save()
        return user.id.__str__()  # gets the stringified version of the ObjectID

    @staticmethod
    def update_user(id, data={}):
        user = User.objects(id=id).first()
        
        # set new values in the user
        for key, val in data.items():
            setattr(user, key, val)
        user.save()

        return user

    @staticmethod
    def delete_user(id):
        if (type(id) != 'string'):
            raise TypeError(f"Invalid id : ${id}")

        user = User.objects(id=id).first()
        if (user == None):
            raise AttributeError(f"No user found with id ${id}")

        user.delete()
