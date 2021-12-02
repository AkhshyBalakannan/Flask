'''MEAL MODEL'''
import uuid
from menu_backend import db

# pylint: disable=no-member


class Meal(db.Model):
    '''Meal Schema'''
    meal_id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50))
    meal_name = db.Column(db.String(20))
    meal_food = db.relationship(
        'Food', secondary='relation', backref=db.backref('food_meals', lazy='dynamic'))

    def __repr__(self):
        '''repr'''
        return f"Meal('{self.meal_name}')"

def create_meal(data):
    '''Add Meal Instance'''
    meal_instance = Meal(meal_name=data['meal_name'], public_id=str(uuid.uuid4()))
    db.session.add(meal_instance)
    db.session.commit()
    return meal_instance


def update_meal(data):
    '''Update meal Instance'''
    meal_instance = Meal.query.filter_by(
        meal_name=data['old_meal_name']).first()
    meal_instance.meal_name = data['new_meal_name']
    db.session.add(meal_instance)
    db.session.commit()
    return meal_instance


def delete_meal(public_id):
    '''Delete meal Instance'''
    meal_instance = Meal.query.filter_by(public_id=public_id).first()
    meal_instance.delete()
    db.session.commit()
