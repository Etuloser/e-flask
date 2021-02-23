from flask import jsonify


def handle_success(data=None, resp_info='success'):
    return jsonify({
        'data': data,
        'resp_info': resp_info,
        'resp_code': 200
    })


def handle_error(data=None, resp_info='error'):
    return jsonify({
        'data': data,
        'resp_info': resp_info,
        'resp_code': 500
    })
