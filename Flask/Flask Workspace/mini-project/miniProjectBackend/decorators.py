from functools import wraps
import jwt 
from miniProjectBackend.models.user import User 
from flask import request, jsonify 
from miniProjectBackend import app

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(
                token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(
                public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

def admin_only(f):
    @wraps(f)
    def decorated(current_user, *args, **kwargs):
        if not current_user.admin:
            return jsonify({'message': 'You Dont have rights'}), 401

        return f(current_user, *args, **kwargs)

    return decorated