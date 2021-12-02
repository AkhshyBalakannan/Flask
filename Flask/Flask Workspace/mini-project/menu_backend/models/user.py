'''USER MODEL'''
import uuid
from menu_backend import db, bcrypt

# pylint: disable=no-member


class User(db.Model):
    '''User Schema'''
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        '''repr'''
        return f"User('{self.username}', '{self.email}')"


def create_user(data):
    '''Create User Instance'''
    hashed_password = bcrypt.generate_password_hash(
        data['password']).decode('utf-8')
    user = User(public_id=str(uuid.uuid4(
    )), username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return user.public_id

def update_user(data, user_instance):
    '''Update User Instance'''
    user_instance.email = data['email']
    user_instance.username = data['username']
    db.session.add(user_instance)
    db.session.commit()


def delete_user(data):
    '''Delete User Instance'''
    user = User.query.filter_by(public_id=data).first()
    db.session.delete(user)
    db.session.commit()
