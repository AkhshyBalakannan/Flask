from menuCard import app
from menuCard import models
from flask import Blueprint, request

food_routes=Blueprint("food_routes", __name__)

Food = models.food.Food
add_Food = models.food.create_food
update_Food = models.food.update_food
delete_Food = models.food.delete_food

data = {
    'food':'',
    'meal':'',
    'relation':'',
}

@food_routes.route('/food', methods=['GET','POST','PATCH'])
def food():
    if request.method == 'GET':
        return data
    if request.method == 'POST':
        food_instance = add_Food(request.form.get('food'))
        return(f'created food {food_instance}')
    if request.method == 'PATCH':
        food_instance = update_Food(request.form.get('old_name'), request.form.get('new_name'))
       
        return(f'created food {food_instance}')


@food_routes.route('/delete/food/<int:id>', methods=['DELETE'])
def food_deletion(id):
    if request.method == 'DELETE':
        delete_Food(id)
        return (f'deleted Food and relation')