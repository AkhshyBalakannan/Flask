from miniProjectBackend import app , db

from flask import redirect, url_for, request, render_template

from miniProjectBackend.models.food import create_relation

add_relation = create_relation


data = {
    'food':'',
    'meal':'',
    'relation':'',
}

@app.route('/db-create')
def create_all():
    db.create_all()

@app.route('/db-drop')
def drop_all():
    db.drop_all()



@app.route('/link', methods=['GET','POST'])
def create_relation():
    if request.method == 'GET':
        return data
    if request.method == 'POST':
        relation_instance = add_relation(food = request.form.get('food'), meal=request.form.get('meal'))
        return(f'created relation {relation_instance}')
   

# ---------------------------------------------------------------------------------

# from miniProjectBackend import app , db, models
# from flask import redirect, url_for, request, render_template

# add_relation = models.food.create_relation

# data = {
#     'food':'',
#     'meal':'',
#     'relation':'',
# }

# @app.route('/dbcreate', methods=["GET"])
# def seed_db():
#     db.create_all()
#     return 'Seeded Db'

# @app.route('/dbdrop', methods=['DELETE'])
# def delete_db():
#     db.drop_all()
#     return 'Dropped Db'

# @app.route('/link', methods=['GET','POST'])
# def relation():
#     if request.method == 'GET':
#         return data
#     if request.method == 'POST':
#         relation_instance = add_relation(food = request.form.get('food'), meal=request.form.get('meal'))
#         return(f'created relation {relation_instance}')
   