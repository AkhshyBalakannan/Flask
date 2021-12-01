'''Common Routes'''
from flask import request
from miniProjectBackend import app, db
from miniProjectBackend.models.food import create_relation
from miniProjectBackend.decorators import token_required, admin_only


@app.route('/db-create')
@token_required
@admin_only
def create_all():
    '''Create database'''
    db.create_all()


@app.route('/db-drop')
@token_required
@admin_only
def drop_all():
    '''Drop database'''
    db.drop_all()


@app.route('/link', methods=['POST'])
@token_required
@admin_only
def relation():
    '''Create Relation'''
    data = request.get_json()
    relation_instance = create_relation(data)
    return f'created relation {relation_instance}'
