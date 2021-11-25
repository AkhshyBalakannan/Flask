from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '1d053a80c2a8d6760b921bd7ed78f1e1'
# to get this key we use secret module in python 
# import secrets 
# secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
# password = 'password@123'
# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:{password}@localhost:3306/miniproject'
db = SQLAlchemy(app)

from miniProjectBackend import routes
