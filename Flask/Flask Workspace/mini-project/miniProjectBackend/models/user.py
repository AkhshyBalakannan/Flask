from miniProjectBackend import db, bcrypt
import uuid



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


def create_user(data):
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = User(public_id=str(uuid.uuid4()), username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(user)
    db.session.commit()


def update_user(data, user_instance):
    user_instance.email = data['email']
    user_instance.username = data['username']
    db.session.add(user_instance)
    db.session.commit()

def delete_user(data):
    user = User.query.filter_by(public_id=data).first()
    db.session.delete(user)
    db.session.commit()
