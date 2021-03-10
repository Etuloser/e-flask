"""
HTTP Status Code:
200 OK
201 Created
202 Accepted
204 No Content

400 Bad Request
403 Forbidden
404 Not Found
405 Method Not Allowed
408 Request Timeout
500 Internal Server Error
"""
from flask import jsonify


def handle_success(data=None, message='success', code='10200'):
    return jsonify({
        'data': data,
        'message': message,
        'code': code,
        'success': True
    })


def handle_error(data=None, message='error', code='10500'):
    return jsonify({
        'data': data,
        'message': message,
        'code': code,
        'success': False
    })
