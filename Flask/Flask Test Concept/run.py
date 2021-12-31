from flask import Flask, request
from flask.json import jsonify
app = Flask(__name__)

app.config["USERNAME"] = "akhshy"
app.config["PASSWORD"] = "password"


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    data = request.get_json()
    if(data["username"] == app.config["USERNAME"] &
       data["password"] == app.config["PASSWORD"]):
        return 'You were logged in'
    elif(request.body.password == app.config["PASSWORD"]):
        return 'Invalid password'
    return 'Invalid username'


if __name__ == '__main__':
    app.run(debug=True)
