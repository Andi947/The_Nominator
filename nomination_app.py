import requests
from flask import Flask, flash, redirect, render_template, request, session, url_for
import sys
import logging
from users_data import *
from nominations_data import *
from result_calculator import *

# sets a secret_key value to run and track the session
app = Flask(__name__)
app.secret_key = 'hwjejfiHhhJdjHg73839'
app.config['SESSION_TYPE'] = 'filesystem'

# assists with logging (not sure as of yet its use)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

# initialising objects and creating lists & dictionary to be used
usersList = UsersData().get_list()
nominationList = NominationsData().get_list()
calculate = CalculatorResult()
results = [1,2,3]
nomineeID_count = []
nominee_counts = {}

# defines the method to send an email containing the user input utilising
# Mailgun's API
def send_simple_message(user, email, username, reason):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxd1d501b9d63946c485beeb236fa2107a.mailgun.org/messages",
        auth=("api", "key-95930168696abf549f49037e039116e0"),
        data={"from": "CFG:IG Group Presentation <mailgun@sandboxd1d501b9d63946c485beeb236fa2107a.mailgun.org>",
              "to": ["ayjaynaylor@gmail.com"],
              "subject": "The Nominator - " + str(user).title() + "'s nomination",
              "text": str(user).title() + "\nnominated: "+ str(username).title() + "\nbecause: " + str(reason) + ".\nPlease let them know the winner: " + str(email)})

# routes to the landing page/ home page / login page. It reads whether a session
# has been created. If false, renders index page that links to login page. If
# true, goes to the user page.
@app.route("/")
def home():
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        return render_template('user.html')

# routes to the login page where a user can input log in details
@app.route("/login", methods=["POST"])
def login():
    return render_template("login.html")

# routes to the user page after checking that the username and password provided
#  are not empty (can be ensured by making entry a requirement on html template)
# If they are empty, it routes to the index/home/landing page
# In future, user details will be checked against database, if authenticated,
# they can continue, if not, try again or sign up where new users will be added.
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

#routes to the nomination page where a user inputs the nomination information
@app.route("/nomination", methods=["POST"])
def nomination_options():
    return render_template("nomination.html", option_list=usersList)

#  routes to the submission page where it creates a nomination object from the
#  the user input and adds the nomination to the nomination list. It then sends
#  the nomination to a stipulated email address
#  In future, it will be added to a database and the admin user can then access
#  the anonymised nominations and results and email the team about the winner.
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

    send_simple_message(your_username, your_email, name, reason)

    return render_template("submission.html")

# routes to the results page where the nomination results are calculated using
# the results_calculator class after which it displays the results
@app.route("/results", methods=["POST"])
def view_nomination_results():
    nomineeID_list = calculate.list_of_nomineeIDs(nominationList)

    nominee_nominationTally = calculate.nomination_per_nominee(nomineeID_list)

    winning_userID = calculate.calculate_winning_nomineeID(nominee_nominationTally)

    winner_name = calculate.winnerID(usersList, winning_userID)
    results[0] = winner_name

    number_of_votes = calculate.no_of_votes(nominee_nominationTally)
    results[1] = number_of_votes

    total_votes = calculate.total_votes(nomineeID_list)
    results[2] = total_votes

    return render_template('results.html', results_list = results)

# a method to define what happens when the logout link is selected. Session is
#  ended and you are redirected to the home/ landing page.
@app.route("/logout")
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
