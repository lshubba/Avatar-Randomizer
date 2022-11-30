from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for
import random
import string

#ENV_FILE = find_dotenv()
#if ENV_FILE:
    #load_dotenv(ENV_FILE)

application = Flask(__name__)
#app.

@application.route("/")
def home():
    return "<p>This is the home page</p>"

@application.route("/login")
def login():
    return "<p>This is the login page</p>"

@application.route("/avatar")
def avatar():
    #Generate hash
    hash = ''.join(random.choice(string.ascii_letters + string.digits) for a in range(16))

    return render_template("avatar.html", link = "https://robohash.org/" + hash + ".png")

if __name__ == '__main__':
    application.run(host="0.0.0.0", port=5001)