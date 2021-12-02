'''FOOD MODEL'''
import uuid
from menu_backend import db, models

# pylint: disable=no-member


class Food(db.Model):
    '''Food Schema'''
    food_id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50))
    food_name = db.Column(db.String(20))

    def __repr__(self):
        '''repr'''
        return f"Food('{self.food_name}')"

def create_food(data):
    '''Create food instance'''
    food_instance = Food(food_name=data['food_name'], public_id=str(uuid.uuid4()))
    db.session.add(food_instance)
    db.session.commit()
    return food_instance


def update_food(data):
    '''Update food instance'''
    food_instance = Food.query.filter_by(
        food_name=data['old_food_name']).first()
    food_instance.food_name = data['new_food_name']
    db.session.add(food_instance)
    db.session.commit()
    return food_instance


def delete_food(public_id):
    '''Delete food instance'''
    food_instance = Food.query.filter_by(public_id=public_id).first()
    db.session.delete(food_instance)
    db.session.commit()


def create_relation(data):
    '''Create Relation with meal'''
    food_instance = Food.query.filter_by(
        public_id=data['food_public_id']).first()
    meal_instance = models.Meal.query.filter_by(
        public_id=data['meal_public_id']).first()
    food_instance.food_meals.append(meal_instance)
    db.session.commit()
    return food_instance
