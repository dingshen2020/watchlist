from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/hello2')
def hello2():
    return '<img src="http://helloflask.com/totoro.gif">'