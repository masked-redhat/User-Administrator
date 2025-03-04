from dotenv import load_dotenv
import os

# load env variables
load_dotenv()


class ServerEnv:
    PORT = int(os.getenv('PORT', '5000'))
    HOST = os.getenv('HOST', 'localhost')


class DatabaseEnv:
    HOST = os.getenv('MONGO_HOST', '127.0.0.1')
    PORT = int(os.getenv('MONGO_PORT', '27017'))
    DB = os.getenv('MONGO_DATABASE')
    USER = os.getenv('MONGO_USER')
    PASSWORD = os.getenv('MONGO_PASS')
    CONN = "users_db_connection"


class SystemEnv:
    ENV = os.getenv('ENV', 'dev')  # if set to 'prod', debug = False
