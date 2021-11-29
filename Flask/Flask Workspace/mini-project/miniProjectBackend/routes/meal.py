from miniProjectBackend.models.meal import create_meal, update_meal, delete_meal
from flask import redirect, url_for, request, render_template, Blueprint

meal_routes=Blueprint("meal_routes", __name__)

data = {
    'food':'',
    'meal':'',
    'relation':'',
}

@meal_routes.route('/cru', methods=['GET','POST','PATCH'])
def meal():
    if request.method == 'GET':
        return data
    if request.method == 'POST':
        meal_instance = create_meal(request.form.get('meal'))
        return(f'created meal{meal_instance}')

    if request.method == 'PATCH':
        meal_instance = update_meal(request.form.get('old_name'), request.form.get('new_name'))
       
        return(f'created Meal {meal_instance}')

@meal_routes.route('/delete/<int:id>', methods=['DELETE'])
def meal_deletion(id):
    if request.method == 'DELETE':
        delete_meal(id)
        return (f'deleted Meal and relation')