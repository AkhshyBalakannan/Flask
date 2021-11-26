from flask import Flask 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = ''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from menuCard import route

from .routes.food import food_routes
from .routes.meal import meal_routes

app.register_blueprint(food_routes, url_prefix="/food")
app.register_blueprint(meal_routes, url_prefix="/meal")