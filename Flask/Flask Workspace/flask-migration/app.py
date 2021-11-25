from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = '1d053a80c2a8d6760b921bd7ed78f1e1'
# to get this key we use secret module in python 
# import secrets 
# secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@123@3306.hostedresource.com/miniproject'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# this code is to try the migrate functions 
# command line codes are flask db init to create migration folder
# flask db migrate is to create the migration file sql query 
# we can add commit message by giving flask db migrate -m "message"
# Lastly to make changes to the db we give flask db upgrade 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    # email = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'{self.username}'


@app.route('/', methods=['GET'])
def home():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)
