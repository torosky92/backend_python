from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

def error_response(status_code, message=None):
    payload = {'status': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['data'] = message
    response = jsonify(payload)
    return response

def not_acceptable(message):
    return error_response(406, message)

def not_found(message):
    return error_response(404, message)

def success_request(response):
    payload = {'status': HTTP_STATUS_CODES.get(200, 'done')}
    payload['data'] = response
    response = jsonify(payload)
    return response
