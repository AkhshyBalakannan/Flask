'''Service file contains helper function'''
import datetime
import jwt
from flask import make_response, jsonify
from miniProjectBackend.models.user import User, db
from miniProjectBackend import bcrypt, app

# pylint disable:no-member

def promote_user(public_id):
    '''To promote user to admin Role'''
    user = User.query.filter_by(public_id=public_id).first()
    user.admin = True
    db.session.commit()


def generate_token(auth):
    '''To generate token used as for login access'''
    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401,
                             {'WWW-Authenticate': 'Basic realm="Login required!"'})

    user = User.query.filter_by(username=auth.username).first()

    if not user:
        return make_response('Could not verify', 401,
                             {'WWW-Authenticate': 'Basic realm="Login required!"'})

    if bcrypt.check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token': token})

    return make_response('Could not verify', 401,
                         {'WWW-Authenticate': 'Basic realm="Login required!"'})
