class InvalidEventError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"Lambda ApiGateway Event has an invalid body, {self.message}"
        return "Lambda ApiGateway Event is invalid"
