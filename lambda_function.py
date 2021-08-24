import json

from lambda_api_gateway_utils import get_route_key
from repository.developer_repository import DynamoDeveloperRepository
from request_handlers.default_request_handler import DummyHandler
from request_handlers.delete_request_handler import DeleteDeveloperRequestHandler
from request_handlers.get_request_handler import GetDeveloperRequestHandler, ListDeveloperRequestHandler
from request_handlers.put_request_handler import PutDeveloperRequestHandler

Handlers = {
    "PUT /developers": PutDeveloperRequestHandler,
    "DELETE /developers/{id}": DeleteDeveloperRequestHandler,
    "GET /developers/{id}": GetDeveloperRequestHandler,
    "GET /developers": ListDeveloperRequestHandler,
    "default": DummyHandler
}

repository = DynamoDeveloperRepository("software-engineers-table")


def lambda_handler(event, context):
    print_request_info(event=event)
    handler = get_handler_for_request(event=event)
    result = handler.process_request()
    print('Ended event processing')
    return result


def print_request_info(event):
    headers = event.get("headers", {})
    request_context = event.get("requestContext", {})
    print('Received incoming event:\n'
          f'User Agent: [{headers["user-agent"]}]\n'
          f'Ip:[{headers["x-forwarded-for"]}]\n'
          f'Host:[{headers["host"]}]\n'
          f'time:[{request_context["time"]}]')


def get_handler_for_request(event):
    route_key = get_route_key(event=event)
    print('Identified routeKey on event: {0}'.format(route_key))
    handler_type = Handlers.get(route_key, Handlers["default"])
    return handler_type(event=event, repository=repository)
