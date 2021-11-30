from flask import Flask
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 


app = Flask(__name__)

app.config['SECRET_KEY'] = '1d053a80c2a8d6760b921bd7ed78f1e1'
# to get this key we use secret module in python 
# import secrets 
# secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
# password = 'password@123'
# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:{password}@localhost:3306/miniproject'

db = SQLAlchemy(app)

migrate = Migrate(app, db)

bcrypt = Bcrypt()

from miniProjectBackend import route

from .routes.food import food_routes
from .routes.meal import meal_routes
from .routes.auth import auth_routes

app.register_blueprint(food_routes, url_prefix="/food")
app.register_blueprint(meal_routes, url_prefix="/meal")
app.register_blueprint(auth_routes, url_prefix="/user")


