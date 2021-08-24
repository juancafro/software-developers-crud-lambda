from request_handlers.lambda_api_request_handler import LambdaApiRequestHandler


class DummyHandler(LambdaApiRequestHandler):
    def __init__(self, event, repository):
        super().__init__(event, repository)

    def is_valid_request(self):
        return True

    def execute(self):
        raise NotImplementedError
