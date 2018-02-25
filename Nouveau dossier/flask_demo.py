
from flask import Flask

app = Flask(__name__)
#"ddddddddddddd"
@app.route("/")
@app.route("/index")

def home():

    return "Hi there"

@app.route("/SayHello/<name>")

def say_hello(name):

    return "Hello {}".format(name)
app.run()

