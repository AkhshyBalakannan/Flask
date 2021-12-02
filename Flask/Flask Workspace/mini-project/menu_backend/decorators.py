'''Custom Decorators'''
from functools import wraps
from flask import request, jsonify
import jwt

from menu_backend.models.user import User
from menu_backend import app


def token_required(func):
    '''Decorator check for validate user'''
    @wraps(func)
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
        except:  # pylint disable:bare-except
            return jsonify({'message': 'Token is invalid!'}), 401

        return func(current_user, *args, **kwargs)

    return decorated


def admin_only(func):
    '''Role based Decorator'''
    @wraps(func)
    def decorated(current_user, *args, **kwargs):
        if not current_user.admin:
            return jsonify({'message': 'You Dont have rights'}), 401

        return func(current_user, *args, **kwargs)

    return decorated
