from miniProjectBackend import app , db
from flask import redirect, url_for, request, render_template
from miniProjectBackend.models.food import create_relation


@app.route('/db-create')
def create_all():
    db.create_all()

@app.route('/db-drop')
def drop_all():
    db.drop_all()


@app.route('/link', methods=['POST'])
def relation():
    data = request.get_json()
    relation_instance = create_relation(data)
    return(f'created relation {relation_instance}')
