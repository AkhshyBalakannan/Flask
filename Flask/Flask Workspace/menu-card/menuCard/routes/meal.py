from menuCard import app,models

from flask import redirect, url_for, request, render_template
from flask import Blueprint, request

meal_routes=Blueprint("meal_routes", __name__)


Meal = models.meal.Meal
add_Meal = models.meal.create_meal
update_Meal = models.meal.update_meal
delete_Meal = models.meal.delete_meal

data = {
    'food':'',
    'meal':'',
    'relation':'',
}

@meal_routes.route('/meal', methods=['GET','POST','PATCH'])
def meal():
    if request.method == 'GET':
        return data
    if request.method == 'POST':
        meal_instance = add_Meal(request.form.get('meal'))
        return(f'created meal{meal_instance}')

    if request.method == 'PATCH':
        meal_instance = update_Meal(request.form.get('old_name'), request.form.get('new_name'))
       
        return(f'created Meal {meal_instance}')

@meal_routes.route('/delete/meal/<int:id>', methods=['DELETE'])
def meal_deletion(id):
    if request.method == 'DELETE':
        delete_Meal(id)
        return (f'deleted Meal and relation')