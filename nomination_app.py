import requests
from flask import Flask, flash, redirect, render_template, request, session, url_for
import sys
import logging
from users_data import *
from nominations_data import *
from result_calculator import *

app = Flask(__name__)
app.secret_key = 'hwjejfiHhhJdjHg73839'
app.config['SESSION_TYPE'] = 'filesystem'

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

usersList = UsersData().get_list()
nominationList = NominationsData().get_list()
calculate = CalculatorResult()
results = [1,2,3]
nomineeID_count = []
nominee_counts = {}

def send_simple_message(user, email, username, reason):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxd1d501b9d63946c485beeb236fa2107a.mailgun.org/messages",
        auth=("api", "key-95930168696abf549f49037e039116e0"),
        data={"from": "GFG:IG Group Presentation <mailgun@sandboxd1d501b9d63946c485beeb236fa2107a.mailgun.org>",
              "to": ["ayjaynaylor@gmail.com"],
              "subject": "The Nominator - " + str(user) + "'s nomination",
              "text": str(user) + "\n nominated "+ str(username) + "\n because: " + str(reason) + ".\n Please let them know the winner: " + str(email)})


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
    username = len(POST_USERNAME)
    POST_PASSWORD = str(request.form['password'])
    password = len(POST_USERNAME)

    if (username > 0) and (password > 0):
        session['logged_in'] = True
    else:
        flash('wrong password')

    return home()
# code for login authentication to be included in the near future
    # for i in usersList:
    #     if i.get_username() == POST_USERNAME:
    #         if i.get_user_password == POST_PASSWORD:
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
    your_email = form_data["your_email"]
    nominee_ID = form_data["nominee"]
    reason = form_data["reason"]

    userID = ""
    for i in usersList:
        if your_username == i.username:
            userID = i.userID
            print userID
        else:
            userID = len(usersList)-1

    new_nomination = Nomination(userID, nominee_ID, reason)
    nominationList.append(new_nomination)

    nominee_names = {}
    for i in usersList:
        nominee_names[int(i.userID)] = str(i.username)

    name = str(nominee_names[int(nominee_ID)])

    # send_simple_message(your_username, your_email, name, reason)

    return render_template("submission.html")

@app.route("/results", methods=["POST"])
def view_nomination_results():
    nomineeID_list = calculate.list_of_nomineeIDs(nominationList)

    nominee_nominationTally = calculate.calculate_nominee_nominations(nomineeID_list)

    winning_userID = calculate.calculate_winning_nomineeID(nominee_nominationTally)

    winner_name = calculate.winnerID(usersList, winning_userID)
    results[0] = winner_name

    number_of_votes = calculate.no_of_votes(nominee_nominationTally)
    results[1] = number_of_votes

    total_votes = calculate.total_votes(nomineeID_list)
    results[2] = total_votes

    return render_template('results.html', results_list = results)

@app.route("/logout")
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
