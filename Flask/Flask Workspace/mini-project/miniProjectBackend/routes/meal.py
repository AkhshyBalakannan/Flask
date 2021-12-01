'''Meal Route'''
from flask import request, Blueprint, jsonify
from miniProjectBackend.models.meal import Meal, create_meal, update_meal, delete_meal
from miniProjectBackend.decorators import token_required, admin_only


meal_routes = Blueprint("meal_routes", __name__)

# pylint: disable=unused-argument



@meal_routes.route('/all', methods=['GET'])
@token_required
def meal(current_user):
    '''Get All Meal'''
    datas = Meal.query.all()
    output = []

    for data in datas:
        meal_data = {}
        meal_data['name'] = data.meal_name
        meal_data['public_id'] = data.public_id
        output.append(meal_data)

    return jsonify(output)


@meal_routes.route('/create', methods=['POST'])
@token_required
@admin_only
def meal_create(current_user):
    '''Post Create Meal'''
    data = request.get_json()
    meal_instance = create_meal(data)
    return f'Created Meal {meal_instance}'


@meal_routes.route('/update', methods=['PATCH'])
@token_required
@admin_only
def meal_update(current_user):
    '''Patch Update Meal'''
    data = request.get_json()
    meal_instance = update_meal(data)
    return f'Updated Meal {meal_instance}'


@meal_routes.route('/delete/<public_id>', methods=['DELETE'])
@token_required
@admin_only
def meal_deletion(current_user, public_id):
    '''Delete - Delete Meal'''
    delete_meal(public_id)
    return 'Deleted meal and relation'
