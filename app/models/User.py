from mongoengine import *


class User(Document):
    name = StringField(required=True, unique=True,
                       min_length=3, max_length=50)
    email = StringField(required=True, unique=True, index=True)
    password = StringField(required=True, min_length=8)

    meta = {
        'collection': 'users',
        'indexes': [
            'email'
        ]
    }
