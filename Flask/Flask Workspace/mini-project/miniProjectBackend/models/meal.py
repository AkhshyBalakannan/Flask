from miniProjectBackend import models
from miniProjectBackend import db
import uuid



# Meal class for db
class Meal(db.Model):
    meal_id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), default=str(uuid.uuid4()))
    meal_name = db.Column(db.String(20))
    meal_food = db.relationship(
        'Food', secondary='relation', backref=db.backref('food_meals', lazy='dynamic'))


# add meal
def create_meal(data):
    meal_instance = Meal(meal_name=data['meal_name'])
    db.session.add(meal_instance)
    db.session.commit()
    return meal_instance


# Update meal
def update_meal(old_meal_name, new_meal_name):
    meal_instance = Meal.query.filter_by(
        meal_name=old_meal_name).first()
    meal_instance.meal_name = new_meal_name
    db.session.add(meal_instance)
    db.session.commit()
    return meal_instance


# Delete meal
def delete_meal(id):
    meal_instance = Meal.query.filter_by(meal_id=id).first()
    db.session.delete(meal_instance)
    db.session.commit()
