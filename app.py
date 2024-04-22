
from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/")
def home():
    name = request.args.get("user")
    if name == None:
        return render_template("index.html")
    elif name == "bob":
        return "Hello " + name
    else: 
        return "User not recognized"
    

