'''Food Route'''
from flask import Blueprint, request, jsonify
from miniProjectBackend.models.food import Food, create_food, update_food, delete_food
from miniProjectBackend.decorators import token_required, admin_only


food_routes = Blueprint("food_routes", __name__)

# pylint: disable=unused-argument


@food_routes.route('/all', methods=['GET'])
@token_required
def food(current_user):
    '''Get All Food'''
    datas = Food.query.all()
    output = []

    for data in datas:
        food_data = {}
        food_data['name'] = data.food_name
        food_data['public_id'] = data.public_id
        output.append(food_data)

    return jsonify(output)


@food_routes.route('/create', methods=['POST'])
@token_required
@admin_only
def food_create(current_user):
    '''Post Create Food'''
    data = request.get_json()
    food_instance = create_food(data)
    return f'created food {food_instance}'


@food_routes.route('/update', methods=['PATCH'])
@token_required
@admin_only
def food_update(current_user):
    '''Patch Update Food'''
    data = request.get_json()
    food_instance = update_food(data)
    return f'created food {food_instance}'


@food_routes.route('/delete/<public_id>', methods=['DELETE'])
@token_required
@admin_only
def food_deletion(current_user, public_id):
    '''Delete - Delete Food'''
    delete_food(public_id)
    return 'Deleted Food and relation'
