from miniProjectBackend import db, models
import uuid



# food class for db
class Food(db.Model):
    food_id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), default=str(uuid.uuid4()))
    food_name = db.Column(db.String(20))


# Add food
def create_food(data):
    food_instance = Food(food_name=data['food_name'])
    db.session.add(food_instance)
    db.session.commit()
    return food_instance


# Update food
def update_food(old_food_name, new_food_name):
    food_instance = Food.query.filter_by(
        food_name=old_food_name).first()
    food_instance.food_name = new_food_name
    db.session.add(food_instance)
    db.session.commit()
    return food_instance


# Delete food
def delete_food(id):
    food_instance = Food.query.filter_by(food_id=id).first()
    db.session.delete(food_instance)
    db.session.commit()


# Create Relation with meal
def create_relation(data):
    food_instance = Food.query.filter_by(public_id=data['food_public_id']).first()
    meal_instance = models.Meal.query.filter_by(public_id=data['meal_public_id']).first()
    food_instance.food_meals.append(meal_instance)
    db.session.commit()
    return food_instance
