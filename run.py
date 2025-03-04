from app import *


def main():
    app = create_flask_app()

    connect_db()

    return app


# for gunicorn
app = main()
