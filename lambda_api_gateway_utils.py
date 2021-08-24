import json

from exceptions.event_exceptions import InvalidEventError


def get_json_body(event,default=None):
    body = event.get("body", None)
    if not body:
        return default
    return json.loads(body)


def get_path_parameter(event, param_name):
    path_parameters = event.get("pathParameters", {})
    return path_parameters.get(param_name,None)


def get_route_key(event):
    return event.get("routeKey", None)


def json_body_has_required_parameters(json_object, required_params):
    for field in required_params:
        if field not in json_object:
            return False
    return True
