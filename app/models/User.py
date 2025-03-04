from mongoengine import Document, StringField
from env import DatabaseEnv as db


class User(Document):
    name = StringField(required=True, min_length=3, max_length=50)
    email = StringField(required=True, unique=True)
    password = StringField(required=True, min_length=8)

    meta = {
        'db_alias': db.CONN,
        'collection': 'users'
    }
