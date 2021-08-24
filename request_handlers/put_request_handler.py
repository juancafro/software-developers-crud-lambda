from abc import ABC
from datetime import date

from bson import ObjectId

from lambda_api_gateway_utils import get_json_body, json_body_has_required_parameters
from request_handlers.lambda_api_request_handler import LambdaApiRequestHandler

required_fields = ["fistName", "lastName", "position", "experienceYears", "status", "salary"]


class PutDeveloperRequestHandler(LambdaApiRequestHandler, ABC):

    def __init__(self, event, repository):
        LambdaApiRequestHandler.__init__(self, event=event, repository=repository)
        self.body = get_json_body(event)
        print(f'PutDeveloperRequestHandler > Starting new Put developer request')

    def is_valid_request(self):
        print('PutDeveloperRequestHandler > Validating request')
        if not self.body:
            self.errors.append("Invalid body value")
            return False
        if not json_body_has_required_parameters(self.body, required_fields):
            self.errors.append("Body hasn´t the mandatory parameters")
            return False
        return True

    def execute(self):
        print('PutDeveloperRequestHandler > Starting execution')
        if "id" not in self.body:
            self.body["id"] = str(ObjectId())
        self.body["enrollmentDate"] = date.today().strftime("%B %d, %Y")
        self.repository.put(self.body)
        self.result = {"id": self.body["id"], "message": "employee created!!"}
        print('PutDeveloperRequestHandler > Finished execution')

