from flask import jsonify
from werkzeug.exceptions import HTTPException

def bad_request(status_code):
    messages = {
        404: "404 Not Found.",
        405: "405 Invalid input.",
    }
    response = jsonify({'message': messages.get(status_code, '{} Error'.format(status_code))})
    response.status_code = status_code
    return response


def make_json_error(ex):
    response = jsonify(message=str(ex))
    response.status_code = (ex.code
                            if isinstance(ex, HTTPException)
                            else 500)
    return response
