import requests
from requests import Request, Session
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
app.secret_key = 'hwjejfiHhhJdjHg73839'
app.config['SESSION_TYPE'] = 'filesystem'

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

users = UsersData().get_nominator_users()
usersList = UsersData().get_list()
nominationList = NominationsData().get_list()
calculate = CalculatorResult()
results = [1,2,3]

nomineeID_count = []
nominee_counts = {}

def send_simple_message(email, username, reason):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxd1d501b9d63946c485beeb236fa2107a.mailgun.org/messages",
        auth=("api", "key-95930168696abf549f49037e039116e0"),
        data={"from": "AdminUser <mailgun@sandboxd1d501b9d63946c485beeb236fa2107a.mailgun.org>",
              "to": ["ayjaynaylor@gmail.com"],
              "subject": "The Nominator - " + str(your_username) + " nomination",
              "text": str(your_username) + "\n nominated "+ str(username) + "\n because: " + str(reason) + ".\n Please let them know the winner: " + str(your_email)})

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
    print POST_USERNAME
    username = len(POST_USERNAME)
    print username
    POST_PASSWORD = str(request.form['password'])
    print POST_PASSWORD
    password = len(POST_USERNAME)
    print password

    if (username > 0) and (password > 0):
        session['logged_in'] = True
    else:
        flash('wrong password')

    return home()
    # for i in users:
    #     if users[i].get_username() == POST_USERNAME:
    #         if user[i].get_user_password == POST_PASSWORD:
            #     session['logged_in'] = True
            #     return session['logged_in']
            # else:
            #     flash('wrong password!')

@app.route("/nomination", methods=["POST"])
def nomination_options():
    return render_template("nomination.html", option_list=usersList)

@app.route("/submission", methods=["POST"])
def submission():
    form_data = request.form
    your_username = form_data["your_username"]
    print your_username
    your_email = form_data["your_email"]
    print your_email
    nominee_ID = form_data["nominee"]
    print nominee_ID
    reason = form_data["reason"]
    print reason
    userID = ""
    for i in usersList:
        if your_username == i.username:
            userID = i.userID
            print userID
        else:
            userID = len(usersList)-1
    new_nomination = Nomination(userID, nominee_ID, reason)
    print new_nomination
    nominationList.append(new_nomination)
    print nominationList
    username = str(calculate.winnerID(users, nominee_ID))
    print username
    send_simple_message(your_username, your_email, username, reason)
    print "You have submitted " + your_username + "! Your e-mail is: " + your_email + ". You nominated " + username + " because: " + reason + "."
    return render_template("submission.html")

@app.route("/results", methods=["POST"])
def view_nomination_results():
    print nominationList

    nomineeID_list = calculate.list_of_nomineeIDs(nominationList)
    print nomineeID_list

    nominee_nominationTally = calculate.calculate_nominee_nominations(nomineeID_list)
    print nominee_nominationTally

    winning_userID = calculate.calculate_winning_nomineeID(nominee_nominationTally)
    print winning_userID

    winner_name = calculate.winnerID(users, winning_userID)
    print winner_name
    results[0] = winner_name

    number_of_votes = calculate.no_of_votes(nominee_nominationTally)
    print number_of_votes
    results[1] = number_of_votes

    total_votes = calculate.total_votes(nomineeID_list)
    print total_votes
    results[2] = total_votes

    return render_template('results.html', results_list = results)

@app.route("/logout")
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('home'))

if __name__ == "__main__":
    #
    # sess.init_app(app)

    app.run(debug=True, use_reloader=True)
