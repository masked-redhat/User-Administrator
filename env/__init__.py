from app.utils import load_env

# file to search for env variables
env_file = ".env"

# load env variables
env_vars = load_env(env_file)


class ServerEnv:
    PORT = int(env_vars.get('PORT', '5000'))
    HOST = env_vars.get('HOST', 'localhost')


class DatabaseEnv:
    HOST = env_vars.get('MONGO_HOST', '127.0.0.1')
    PORT = int(env_vars.get('MONGO_PORT', '27017'))
    DB = env_vars.get('MONGO_DATABASE')
    USER = env_vars.get('MONGO_USER')
    PASSWORD = env_vars.get('MONGO_PASS')
