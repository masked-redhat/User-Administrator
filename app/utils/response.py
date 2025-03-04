class SendResponse:
    """A convinient way to handle responses in json format"""

    @staticmethod
    def send(message: str = "", status_code: int = 200, data: dict = {}):
        """Creates a custom response in flask application"""
        return {'message': message, **data}, status_code

    @staticmethod
    def ok(message: str = "", data: dict = {}):
        return SendResponse.send(message, 200, data)

    @staticmethod
    def bad(message: str = "Invalid request", data: dict = {}):
        return SendResponse.send(message, 400, data)

    @staticmethod
    def server_error(message: str = "Internal server error", data: dict = {}):
        return SendResponse.send(message, 500, data)

    @staticmethod
    def no_content():
        return SendResponse.send("", 204)

    @staticmethod
    def created(message: str = "Created", data: dict = {}):
        return SendResponse.send(message, 201, data)
