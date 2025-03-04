from mongoengine import *
from env import DatabaseEnv as db


class User(Document):
    name = StringField(required=True, unique=True,
                       min_length=3, max_length=50)
    email = StringField(required=True, unique=True, index=True)
    password = StringField(required=True, min_length=8)

    meta = {
        'db_alias': db.CONN,
        'collection': 'users',
        'indexes': [
            'email'
        ]
    }
