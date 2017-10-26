import requests
from flask import Flask, render_template, request

app = Flask(__name__)

def send_simple_message(email, username, reason):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxd1d501b9d63946c485beeb236fa2107a.mailgun.org/messages",
        auth=("api", "key-95930168696abf549f49037e039116e0"),
        data={"from": "AdminUser <mailgun@sandboxd1d501b9d63946c485beeb236fa2107a.mailgun.org>",
              "to": [email],
              "subject": "The Nominator - Your nomination",
              "text": "Thank you for nominating!\n You nominated "+ str(username) + "\n because: " + str(reason)})

@app.route("/")
def index():
    # print "Hello Nominator!"
    return render_template("index.html")

@app.route("/nomination", methods=["POST"])
def nomination():
    # print "Let's Nominate"
    return render_template("nomination.html")

@app.route("/submission", methods=["POST"])
def submission():
    form_data = request.form
    email = form_data["email"]
    username = form_data["username"]
    reason = form_data["reason"]
    send_simple_message(email, username, reason)
    return "You have submitted! Your e-mail is: " + email + ". You nominated " + username + " because: " + reason + "."

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
