from app import create_flask_app, connect_db, shutdown_db
from env import ServerEnv as _server
from env import SystemEnv as _system


def main():
    # create the flask application
    app = create_flask_app()

    # connect database
    connect_db()

    # run the flask application
    app.run(debug=_system.ENV == 'dev', port=_server.PORT, host=_server.HOST)


def cleanup():
    """Clean up function when application is supposed to be closing"""
    print("Shutting down gracefully...")
    shutdown_db()
    print("Application closed successfully")


if __name__ == '__main__':
    try:
        main()
    finally:
        # clean up
        cleanup()
