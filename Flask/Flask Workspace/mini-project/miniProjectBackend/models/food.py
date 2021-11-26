from miniProjectBackend import db, models


# food class for db
class Food(db.Model):
    food_id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(20))


# Add food
def create_food(name):
    food_instance = Food(food_name=name)
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
def create_relation(food, meal):
    food_instance = Food.query.filter_by(food_name=food).first()
    meal_instance = models.Meal.query.filter_by(meal_name=meal).first()
    food_instance.food_meals.append(meal_instance)
    db.session.commit()
    return food_instance
