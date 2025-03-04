from app.models.User import User


class UserService:
    @staticmethod
    def get_users():
        users = User.objects()
        return users

    @staticmethod
    def get_user_by_id(id):
        user = User.objects(id=id).first()
        return user

    @staticmethod
    def create_user(data):
        user = User(name=data['name'], email=data['email'],
                    password=data['password'])
        user.save()
        return user.id.__str__()

    @staticmethod
    def update_user(id, data={}):
        user = User.objects(id=id).first()
        for key, val in data.items():
            setattr(user, key, val)
        user.save()

        return user

    @staticmethod
    def delete_user(id):
        user = User.objects(id=id).first()
        user.delete()
