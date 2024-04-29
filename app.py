
from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        name = request.form["us"]
        pw = request.form["pw"]

        if name == None:
            return render_template("index.html")
        elif pw != None and name == "bob" and pw == "123":
            return "Hello " + name
        else: 
            return "User not recognized"
        
@app.route("/signup")
def signup():
    return "signup"
