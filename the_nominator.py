from flask import Flask, render_template, request

app = Flask("The Nominator")

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup", methods=["POST"])
def sign_up():
    return render_template("signup.html")

app.run(debug=True)
