from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for, send_file, request, send_from_directory
from pathlib import Path
import requests
import python_avatars as pa
import random
import string
import requests
import datetime
import re
import json

#Random API key: 947bc7666e0242bbaf55f395d41e5e9a

application = Flask(__name__)



@application.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('action1') == 'Generate':
            return render_main_page()
        if request.form.get('action3') == 'Share':
            return 'Share'
        else:
            pass  # unknown
    elif request.method == 'GET':
        return render_main_page()


@application.route('/download', methods=['POST'])
def download():
    path = './static/avatar.png'
    return send_file(path, as_attachment=True)


@application.route("/login")
def login():
    return render_template("login.html")


@application.route('/cache/<path:filename>')
def cached_avatar(filename):
    return send_from_directory(application.root_path + '/cache/', filename)


def is_cached(name, ext):
    return Path(application.root_path + "/cache/" + name + "." + ext).is_file()


def download_avatar(robohash):
    req = requests.get("https://robohash.org/" + robohash + ".png")
    with open(application.root_path + "/cache/" + robohash + ".png", 'wb') as f:
        f.write(req.content)


def render_main_page():
    # generate random name
    apiResponse = requests.get('https://randomuser.me/api/')
    data = json.loads(apiResponse.content)
    name = data["results"][0]["name"]["first"]
    #roboName = re.sub(r'\W+', '', str(apiResponse.content))[1:]
    # generate robohash
    # TODO: use cookie as an optional source of hash
    robohash = ''.join(random.choice(string.ascii_letters + string.digits) for a in range(16))
    # check local proxy cache first and download avatar if needed
    if not is_cached(robohash, "png"):
        download_avatar(robohash)
    # render main page, pointing to a locally cached avatar
    return render_template("avatar.html", robohash=robohash, year=datetime.date.today().year, robotName=name)


if __name__ == '__main__':
    application.run(host="0.0.0.0", port=5001)
