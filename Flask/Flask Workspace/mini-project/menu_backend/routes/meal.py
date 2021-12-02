'''Meal Route'''
from flask import request, Blueprint, jsonify
from menu_backend.models.meal import Meal, create_meal, update_meal, delete_meal
from menu_backend.decorators import token_required, admin_only
from menu_backend.service import meal_list, menu_card


meal_routes = Blueprint("meal_routes", __name__)

# pylint: disable=unused-argument


@meal_routes.route('/all', methods=['GET'])
@token_required
def meal_with_food(current_user):
    '''Get All Meal with food'''
    output = menu_card()

    return jsonify(output)


@meal_routes.route('/types', methods=['GET'])
@token_required
def list_of_meal(current_user):
    '''Get All Meal Type'''
    output = meal_list()

    return jsonify(output)


@meal_routes.route('/create', methods=['POST'])
@token_required
@admin_only
def meal_create(current_user):
    '''Post Create Meal
    Data must be given with 
    meal_name
    '''
    data = request.get_json()
    meal_instance = create_meal(data)
    return f'Created Meal {meal_instance}'


@meal_routes.route('/update', methods=['PATCH'])
@token_required
@admin_only
def meal_update(current_user):
    '''Patch Update Meal
    Data must be given with 
    old_meal_name, new_meal_name
    '''
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
