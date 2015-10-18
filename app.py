from flask import Flask, render_template, session, request
import sqlite3

app = Flask(__name__)


conn = sqlite3.connect("backend.db")

@app.route("/")
@app.route("/home")

def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/myaccount")
def myaccount():
    return render_template("myaccount.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__== "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8000)
