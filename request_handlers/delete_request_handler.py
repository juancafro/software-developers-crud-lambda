from lambda_api_gateway_utils import get_path_parameter
from request_handlers.lambda_api_request_handler import LambdaApiRequestHandler


class DeleteDeveloperRequestHandler(LambdaApiRequestHandler):

    def __init__(self, event, repository):
        LambdaApiRequestHandler.__init__(self, event=event, repository=repository)
        self.id = get_path_parameter(event, "id")
        print(f'DeleteDeveloperRequestHandler > Starting new request with id: [{self.id}]')

    def is_valid_request(self):
        print(f'DeleteDeveloperRequestHandler > Validating request')
        if not self.id:
            return False
        else:
            return True

    def execute(self):
        print(f'DeleteDeveloperRequestHandler >  Starting execution')
        self.repository.delete(self.id)
        self.result = {"id": self.id, "message": "employee deleted!!"}
        print(f'DeleteDeveloperRequestHandler > Finished execution')
