from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for, send_file, request
import python_avatars as pa
import random
import string

#ENV_FILE = find_dotenv()
#if ENV_FILE:
    #load_dotenv(ENV_FILE)

application = Flask(__name__)
#app

@application.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('action1') == 'Create':
            #generate hash
            hash = ''.join(random.choice(string.ascii_letters + string.digits) for a in range(16))
            return render_template("avatar.html", link = "https://robohash.org/" + hash + ".png")
        if request.form.get('action2') == 'Download':
            return 'Download'
        if request.form.get('action3') == 'Share':
            return 'Share'
        else:
            pass # unknown
    elif request.method == 'GET':
            #generate hash
            hash = ''.join(random.choice(string.ascii_letters + string.digits) for a in range(16))
            return render_template("avatar.html", link = "https://robohash.org/" + hash + ".png")

@application.route('/download')
def download():
    path = 'avtar.png'
    return send_file(path, as_attachment=True)

@application.route("/login")
def login():
    return render_template("login.html")

if(__name__ == "__main__"):
    application.run()