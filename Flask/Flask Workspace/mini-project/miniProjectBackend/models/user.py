from miniProjectBackend import db, bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


def create_user(form):
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data, email=form.email.data, password=hashed_password)
    db.session.add(user)
    db.session.commit()


def update_user(user_instance, email, username):
    user_instance.email = email
    user_instance.username = username
    db.session.add(user_instance)
    db.session.commit()


def reset_password(user_instance, old_password, new_password):
    if (user_instance.password == old_password):
        user_instance.password = new_password
        db.session.add(user_instance)
        db.session.commit()
