from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os
import sys
import logging
import users_data
from users_data import *
import nominations_data
from nominations_data import *
from result_calculator import *

app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

users = UsersData().get_nominator_users()
usersList = UsersData().get_list()
nominations = NominationsData().nominator_nominations
data = NominationsData()
calculate = CalculatorResult()

nomineeID_count = []
nominee_counts = {}

def send_simple_message(email, username, reason):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxd1d501b9d63946c485beeb236fa2107a.mailgun.org/messages",
        auth=("api", "key-95930168696abf549f49037e039116e0"),
        data={"from": "AdminUser <mailgun@sandboxd1d501b9d63946c485beeb236fa2107a.mailgun.org>",
              "to": [email],
              "subject": "The Nominator - Your nomination",
              "text": "Thank you for nominating!\n You nominated "+ str(username) + "\n because: " + str(reason)})

# <a href='/logout'>Logout</a>"

@app.route("/")
def home():
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        return render_template('user.html')

@app.route("/login", methods=["POST"])
def login():
    return render_template("login.html")

@app.route("/user", methods=["POST"])
def user():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
    session['logged_in'] = True
    # for i in users:
    #     if users[i].get_username() == POST_USERNAME:
    #         if user[i].get_user_password == POST_PASSWORD:
            #     session['logged_in'] = True
            #     return session['logged_in']
            # else:
            #     flash('wrong password!')
    return home()

@app.route("/nomination", methods=["POST"])
def nomination_options():
    return render_template("nomination.html", option_list=usersList)

@app.route("/submission", methods=["POST"])
def submission():
    form_data = request.form
    your_username = form_data["your_username"]
    your_email = form_data["your_email"]
    nominee_ID = form_data["nominee"]
    reason = form_data["reason"]
    userID = ""
    _hasNext = None
    for i in usersList:
        if your_username == i.username:
            userID = i.userID
            print userID
        else:
            userID = len(users)-1
    new_nomination = Nomination(userID, nominee_ID, reason)
    nominations.append(new_nomination)
    print nominations
    # send_simple_message(email, username, reason)
    print "You have submitted " + your_username + "! Your e-mail is: " + your_email + ". You nominated " + nominee_ID + " because: " + reason + "."
    return render_template("submission.html")

@app.route("/results", methods=["POST"])
def view_nomination_results():

        return 0

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
