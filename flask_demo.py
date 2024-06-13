from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ping", methods = ['GET'])
def pinger():
    return "<p>Hello I am Batman</p>"

@app.route("/json_check", methods = ['GET'])
def json():
    return {"message": "Hi I am JSON"}
