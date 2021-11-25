from miniProjectBackend import app
from miniProjectBackend import models
from flask import redirect, url_for, request, render_template


Food = models.food.Food
add_Food = models.food.create_food
update_Food = models.food.update_food
delete_Food = models.food.delete_food

data = {
    'food':'',
    'meal':'',
    'relation':'',
}

@app.route('/food', methods=['GET','POST','PATCH'])
def food():
    if request.method == 'GET':
        return data
    if request.method == 'POST':
        food_instance = add_Food(request.form.get('food'))
        return(f'created food {food_instance}')
    if request.method == 'PATCH':
        food_instance = update_Food(request.form.get('old_name'), request.form.get('new_name'))
       
        return(f'created food {food_instance}')


@app.route('/delete/food/<int:id>', methods=['DELETE'])
def food_deletion(id):
    if request.method == 'DELETE':
        delete_Food(id)
        return (f'deleted Food and relation')