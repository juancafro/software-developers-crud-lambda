import unittest

import lambda_function


class SimpleTest(unittest.TestCase):

    @staticmethod
    def test_lambda_handler_put_developer():
        event = {
            "version": "2.0",
            "routeKey": "PUT /developers",
            "rawPath": "/developers",
            "rawQueryString": "",
            "headers": {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "cache-control": "no-cache",
                "content-length": "161",
                "content-type": "application/json",
                "host": "4o77czx2c9.execute-api.us-east-1.amazonaws.com",
                "postman-token": "9a72a57b-df65-4df2-8c41-1dd39521d2bf",
                "user-agent": "PostmanRuntime/7.28.3",
                "x-amzn-trace-id": "Root=1-61245907-4034f4fb67219a2467595521",
                "x-forwarded-for": "190.158.136.130",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https"
            },
            "requestContext": {
                "accountId": "876977665967",
                "apiId": "4o77czx2c9",
                "domainName": "4o77czx2c9.execute-api.us-east-1.amazonaws.com",
                "domainPrefix": "4o77czx2c9",
                "http": {
                    "method": "PUT",
                    "path": "/developers",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "190.158.136.130",
                    "userAgent": "PostmanRuntime/7.28.3"
                },
                "requestId": "EjLZPjnAoAMEVHQ=",
                "routeKey": "PUT /developers",
                "stage": "$default",
                "time": "24/Aug/2021:02:27:19 +0000",
                "timeEpoch": 1629772039794
            },
            "body": "{\r\n  \"fistName\": \"Jonas\",\r\n  \"lastName\": \"Smith\",\r\n  \"position\":\"Senior "
                    "Software Engineer\",\r\n  \"experienceYears\":\"7\",\r\n  \"status\":\"ACTIVE\","
                    "\r\n  \"salary\":\"120k\"\r\n}",
            "isBase64Encoded": False
        }
        context = ""
        response = lambda_function.lambda_handler(event, context)

    @staticmethod
    def test_lambda_handler_delete_developer():
        event = {
            "version": "2.0",
            "routeKey": "DELETE /developers/{id}",
            "rawPath": "/developers/6124495fbad3ef86e4e6556d",
            "rawQueryString": "",
            "headers": {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "cache-control": "no-cache",
                "content-length": "0",
                "host": "4o77czx2c9.execute-api.us-east-1.amazonaws.com",
                "postman-token": "147635b5-56f9-4e0c-b248-70b3068f4bfa",
                "user-agent": "PostmanRuntime/7.28.3",
                "x-amzn-trace-id": "Root=1-61245ee5-21e8b948482c14b87ddfd009",
                "x-forwarded-for": "190.158.136.130",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https"
            },
            "requestContext": {
                "accountId": "876977665967",
                "apiId": "4o77czx2c9",
                "domainName": "4o77czx2c9.execute-api.us-east-1.amazonaws.com",
                "domainPrefix": "4o77czx2c9",
                "http": {
                    "method": "DELETE",
                    "path": "/developers/6124495fbad3ef86e4e6556d",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "190.158.136.130",
                    "userAgent": "PostmanRuntime/7.28.3"
                },
                "requestId": "EjPD1gaUIAMEVyg=",
                "routeKey": "DELETE /developers/{id}",
                "stage": "$default",
                "time": "24/Aug/2021:02:52:21 +0000",
                "timeEpoch": 1629773541156
            },
            "pathParameters": {
                "id": "6124495fbad3ef86e4e6556d"
            },
            "isBase64Encoded": False
        }
        context = ""
        response = lambda_function.lambda_handler(event, context)

    @staticmethod
    def test_lambda_handler_get_developer():
        event = {
            "version": "2.0",
            "routeKey": "GET /developers/{id}",
            "rawPath": "/developers/6124495fbad3ef86e4e6556d",
            "rawQueryString": "",
            "headers": {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "cache-control": "no-cache",
                "content-length": "0",
                "host": "4o77czx2c9.execute-api.us-east-1.amazonaws.com",
                "postman-token": "43de76b1-0675-43a4-89a0-c7ede514a986",
                "user-agent": "PostmanRuntime/7.28.3",
                "x-amzn-trace-id": "Root=1-61245e7f-673a441d5336b94265a5978b",
                "x-forwarded-for": "190.158.136.130",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https"
            },
            "requestContext": {
                "accountId": "876977665967",
                "apiId": "4o77czx2c9",
                "domainName": "4o77czx2c9.execute-api.us-east-1.amazonaws.com",
                "domainPrefix": "4o77czx2c9",
                "http": {
                    "method": "GET",
                    "path": "/developers/6124495fbad3ef86e4e6556d",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "190.158.136.130",
                    "userAgent": "PostmanRuntime/7.28.3"
                },
                "requestId": "EjOz5hFzoAMEWNQ=",
                "routeKey": "GET /developers/{id}",
                "stage": "$default",
                "time": "24/Aug/2021:02:50:39 +0000",
                "timeEpoch": 1629773439107
            },
            "pathParameters": {
                "id": "6124495fbad3ef86e4e6556d"
            },
            "isBase64Encoded": False
        }
        context = ""
        response = lambda_function.lambda_handler(event, context)

    @staticmethod
    def test_lambda_handler_list_developers():
        event = {
            "version": "2.0",
            "routeKey": "GET /developers",
            "rawPath": "/developers",
            "rawQueryString": "",
            "headers": {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "cache-control": "no-cache",
                "content-length": "0",
                "host": "4o77czx2c9.execute-api.us-east-1.amazonaws.com",
                "postman-token": "5a2eb80b-7b50-4238-8cce-cd4c21d25794",
                "user-agent": "PostmanRuntime/7.28.3",
                "x-amzn-trace-id": "Root=1-612459b8-0918737479962b545c3861aa",
                "x-forwarded-for": "190.158.136.130",
                "x-forwarded-port": "443",
                "x-forwarded-proto": "https"
            },
            "requestContext": {
                "accountId": "876977665967",
                "apiId": "4o77czx2c9",
                "domainName": "4o77czx2c9.execute-api.us-east-1.amazonaws.com",
                "domainPrefix": "4o77czx2c9",
                "http": {
                    "method": "GET",
                    "path": "/developers",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "190.158.136.130",
                    "userAgent": "PostmanRuntime/7.28.3"
                },
                "requestId": "EjL07jxmIAMEVrQ=",
                "routeKey": "GET /developers",
                "stage": "$default",
                "time": "24/Aug/2021:02:30:16 +0000",
                "timeEpoch": 1629772216964
            },
            "isBase64Encoded": False
        }
        context = ""
        response = lambda_function.lambda_handler(event, context)
