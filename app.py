from app import app, connect_db
from env import ServerEnv as server


def main():
    # connect database
    connect_db()

    # run the flask application
    app.run(debug=True, port=server.PORT, host=server.HOST)


if __name__ == '__main__':
    main()
