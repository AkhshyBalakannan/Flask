from menuCard import db
from menuCard import models


relation = db.Table('relation',
                    db.Column('meal_id', db.Integer,
                              db.ForeignKey('meal.meal_id')),
                    db.Column('food_id', db.Integer,
                              db.ForeignKey('food.food_id'))
                    )


