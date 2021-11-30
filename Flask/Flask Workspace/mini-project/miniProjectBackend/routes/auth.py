from flask import redirect, url_for, request, Blueprint, jsonify
from miniProjectBackend.models.user import User, create_user, update_user, delete_user
from miniProjectBackend.decorators import token_required, admin_only
from miniProjectBackend.service import promote_user, generate_token

auth_routes = Blueprint("auth_routes", __name__)


@auth_routes.route('/all', methods=['GET'])
@token_required
@admin_only
def all_user(current_user):
    datas = User.query.all()
    output = []

    for data in datas:
        user_data = {}
        user_data['public_id'] = data.public_id
        user_data['username'] = data.username
        user_data['email'] = data.email
        user_data['admin'] = data.admin
        output.append(user_data)

    return jsonify(output)

@auth_routes.route('/new', methods=['POST'])
@token_required
@admin_only
def register_user(current_user):
    data = request.get_json()
    create_user(data)
    return jsonify({'message': 'New user created!'})


@auth_routes.route('/login')
def login():
    auth = request.authorization
    res = generate_token(auth)
    return res 


@auth_routes.route('/update', methods=['PATCH'])
@token_required
def user_updation(current_user):
    data = request.get_json()
    update_user(data, current_user)
    return jsonify({'message': 'Updated user!'})


@auth_routes.route('/promote/<public_id>', methods=['PUT'])
@token_required
@admin_only
def user_promotion(current_user,public_id):
    promote_user(public_id)
    return jsonify({'message': 'Promoted user!'})


@auth_routes.route('/delete/<public_id>', methods=['DELETE'])
@token_required
@admin_only
def user_deletion(current_user,public_id):
    delete_user(public_id)
    return jsonify({'message': 'Deleted user!'})