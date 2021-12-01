'''Relation Model'''
from miniProjectBackend import db

# pylint: disable=no-member


relation = db.Table('relation',
                    db.Column('meal_id', db.Integer,
                              db.ForeignKey('meal.meal_id')),
                    db.Column('food_id', db.Integer,
                              db.ForeignKey('food.food_id'))
                    )
