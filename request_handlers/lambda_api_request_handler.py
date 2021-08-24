import json
from abc import ABC, abstractmethod

from bson import ObjectId


class LambdaApiRequestHandler(ABC):
    def __init__(self, event, repository):
        self.operation_id = str(ObjectId())
        self.repository = repository
        self.event = event
        self.result = {}
        self.errors = []
        self.status_code = 0

    @abstractmethod
    def is_valid_request(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    def process_request(self):
        if self.is_valid_request():
            try:
                self.execute()
                self.status_code = 200
            except NotImplementedError as e:
                self.status_code = 404
                self.errors.append("the resource {0} wasn't found".format(self.event["resource"]))
            except Exception as e:
                self.status_code = 500
                self.errors.append("Exception processing Put Request: [{0}]".format(e))
        else:
            self.status_code = 400
        return self.build_result()

    def build_result(self):
        response = {
            'statusCode': self.status_code,
            'headers': {'Content-Type': 'application/json', }
        }
        if self.status_code == 200:
            response["body"] = json.dumps(self.result)
        else:
            response["body"] = json.dumps(self.errors)
        return response
