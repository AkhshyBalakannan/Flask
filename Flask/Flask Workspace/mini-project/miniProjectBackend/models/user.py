from flask import db 

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True ,nullable=False)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    admin = db.Column(db.Boolean(), default=False)
    authenticated = db.Column(db.Boolean, default=False)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False



def create_user(email, username, password):
    user_instance = User(email=email,username=username, password=password)
    db.session.add(user_instance)
    db.session.commit()

def update_user(user_instance, email, username):
    user_instance.email = email
    user_instance.username=username
    db.session.add(user_instance)
    db.session.commit()

def reset_password(user_instance, old_password, new_password)
    if (user_instance.password == old_password):
        user_instance.password = new_password
        db.session.add(user_instance)
        db.session.commit()
