
from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/")
def home():
    name = request.args.get("us")
    pw = request.args.get("pw")

    if name == None:
        return render_template("index.html")
    elif pw != None and name == "bob" and pw == "123":
        return "Hello " + name
    else: 
        return "User not recognized"
    

