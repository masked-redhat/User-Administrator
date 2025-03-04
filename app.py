from app import app
from env import ServerEnv as server


if __name__ == '__main__':

    # run the flask application
    app.run(debug=True, port=server.PORT, host=server.HOST)
