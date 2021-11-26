from miniProjectBackend.models.food import create_food, update_food, delete_food
from flask import Blueprint, request

food_routes=Blueprint("food_routes", __name__)

data = {
    'food':'',
    'meal':'',
    'relation':'',
}

@food_routes.route('/cru', methods=['GET','POST','PATCH'])
def food_CRU():
    if request.method == 'GET':
        return data
    if request.method == 'POST':
        food_instance = create_food(request.form.get('food'))
        return(f'created food {food_instance}')
    if request.method == 'PATCH':
        food_instance = update_food(request.form.get('old_name'), request.form.get('new_name'))
       
        return(f'created food {food_instance}')


@food_routes.route('/delete/<int:id>', methods=['DELETE'])
def food_deletion(id):
    if request.method == 'DELETE':
        delete_food(id)
        return (f'deleted Food and relation')