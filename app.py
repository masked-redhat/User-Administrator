from app import *


def main():
    # create the flask application
    app = create_flask_app()

    # connect database
    connect_db()

    # run the flask application
    app.run(debug=Config.SYSTEM.ENV == 'dev',
            port=Config.SERVER.PORT,
            host=Config.SERVER.HOST)


def cleanup():
    """Clean up function when application is supposed to be closing"""
    print("Shutting down gracefully...")
    shutdown_db()
    print("Application closed successfully")


if __name__ == '__main__':
    try:
        main()
    finally:
        cleanup()
