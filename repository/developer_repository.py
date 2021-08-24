from abc import ABC, abstractmethod

import boto3


class DeveloperRepository(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def put(self, developer):
        pass

    @abstractmethod
    def get(self, developer_id):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def delete(self, developer_id):
        pass


class DynamoDeveloperRepository(DeveloperRepository):

    def __init__(self, table_name):
        super().__init__()
        self.table_name = table_name
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(table_name)

    def get(self, developer_id):
        dynamo_item = self.table.get_item(
            Key={
                'id': developer_id
            })
        response_item = dynamo_item["Item"]
        return response_item

    def list(self):
        response = self.table.scan()
        return response["Items"]

    def delete(self, developer_id):
        self.table.delete_item(
            Key={
                'id': developer_id,
            }
        )

    def put(self, developer):
        result = self.table.put_item(
            Item=developer
        )
        return developer
