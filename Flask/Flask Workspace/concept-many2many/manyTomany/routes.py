from manyTomany import app 

@app.route('/')
def home():
    return 'hello world!'