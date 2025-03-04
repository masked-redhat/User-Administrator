class SendResponse:
    """A convinient way to handle responses in json format"""

    @staticmethod
    def send(message: str = "", status_code: int = 200, data: dict = {}, success: bool = True):
        """Creates a custom response in flask application"""
        return {'message': message, **data, 'success': success}, status_code

    @staticmethod
    def ok(message: str = "", data: dict = {}):
        return SendResponse.send(message, 200, data)

    @staticmethod
    def bad(message: str = "Invalid request", status_code: int = 400, data: dict = {}):
        return SendResponse.send(message, status_code, data, False)

    @staticmethod
    def server_error(message: str = "Internal server error", data: dict = {}):
        return SendResponse.send(message, 500, data, False)

    @staticmethod
    def no_content():
        return SendResponse.send("", 204)

    @staticmethod
    def created(message: str = "Created", data: dict = {}):
        return SendResponse.send(message, 201, data, True)
