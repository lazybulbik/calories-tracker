from loader import app, get_db
from flask import request, jsonify, make_response

import jwt
import utils
import hmac
import hashlib

import json


@app.before_request
def check_token():
    print(request.path)
    if request.path == '/api/auth' or (not request.path.startswith('/api/')):
        return

    token = request.cookies.get('token')

    if token == None:
        return jsonify({'status': 'error', 'message': 'token not found'}), 400

    try:
        user_data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return jsonify({'status': 'error', 'message': 'token expired'}), 400
    except jwt.InvalidTokenError:
        return jsonify({'status': 'error', 'message': 'invalid token'}), 400