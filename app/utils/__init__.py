from dotenv import dotenv_values


def load_env(path):
    """Loads environment variables"""
    env_vars = dotenv_values(path)
    return env_vars
