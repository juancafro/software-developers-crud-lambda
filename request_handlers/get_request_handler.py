from lambda_api_gateway_utils import get_path_parameter
from request_handlers.lambda_api_request_handler import LambdaApiRequestHandler


class GetDeveloperRequestHandler(LambdaApiRequestHandler):

    def __init__(self, event, repository):
        LambdaApiRequestHandler.__init__(self, event=event, repository=repository)
        self.id = get_path_parameter(event,"id")
        print(f'GetDeveloperRequestHandler > Starting new request with id: [{self.id}]')

    def is_valid_request(self):
        print('GetDeveloperRequestHandler > Validating request')
        if not self.id:
            return False
        else:
            return True

    def execute(self):
        print(f'GetDeveloperRequestHandler > Starting execution')
        self.result=self.repository.get(self.id)
        print('GetDeveloperRequestHandler > Finished execution')


class ListDeveloperRequestHandler(LambdaApiRequestHandler):

    def __init__(self, event, repository):
        LambdaApiRequestHandler.__init__(self, event=event, repository=repository)
        print(f'ListDeveloperRequestHandler > Starting new request')

    def is_valid_request(self):
        return True

    def execute(self):
        print(f'ListDeveloperRequestHandler > Starting execution')
        self.result=self.repository.list()
        print(f'ListDeveloperRequestHandler > Finished execution')
