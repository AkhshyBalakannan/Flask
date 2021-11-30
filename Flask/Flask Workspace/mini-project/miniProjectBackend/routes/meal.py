from miniProjectBackend.models.meal import Meal, create_meal, update_meal, delete_meal
from flask import redirect, url_for, request, render_template, Blueprint, jsonify
from miniProjectBackend.decorators import token_required, admin_only


meal_routes=Blueprint("meal_routes", __name__)


@meal_routes.route('/all', methods=['GET'])
@token_required
def meal(current_user):
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
    data = request.get_json()
    meal_instance = create_meal(data)
    return(f'created food {meal_instance}')


@meal_routes.route('/update', methods=['PATCH'])
@token_required
@admin_only
def meal_update(current_user):
    data = request.get_json()
    meal_instance = update_meal(data)
    return(f'created food {meal_instance}')


@meal_routes.route('/delete/<public_id>', methods=['DELETE'])
@token_required
@admin_only
def meal_deletion(current_user,public_id):
    delete_meal(public_id)
    return (f'deleted Food and relation')
