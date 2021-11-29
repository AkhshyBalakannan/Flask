from werkzeug.exceptions import PreconditionFailed
from miniProjectBackend.models.meal import create_meal, update_meal, delete_meal
from flask import redirect, url_for, request, render_template, Blueprint, flash, jsonify
from flask_login import login_user, current_user, logout_user
from miniProjectBackend.models.user import User
from miniProjectBackend.forms.auth import LoginForm,RegistrationForm
from miniProjectBackend import bcrypt


auth_routes = Blueprint("auth_routes", __name__)

data = {
    'food': '',
    'meal': '',
    'relation': '',
}

@auth_routes.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        User.create_user(form)
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    for f in form:
        if f.id == "csrf_token":
            print(f)
            return str(f)
    return 

@auth_routes.route('/login', methods=['GET', 'POST', 'PATCH'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            print('login failed')
            return form


@auth_routes.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
