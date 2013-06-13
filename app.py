from __future__ import print_function
from flask import Flask, request, json, render_template
from subprocess import call
from pprint import pprint
import gifMachine
import random
import flask
import sys

app = Flask(__name__)

ROOT_URL = "http://bateyhomeserver/rand/"
OUTPUT_DIR = "/var/www/rand/"

@app.route('/')
def root():
    return render_template("frontpage.html")

@app.route('/makegif', methods = ['POST'])
def make_gif():
    toReturn = ''

    # Takes the post request and calls the build_gif params of gifMachine
    if request.json:
        toReturn = gifMachine.build_gif(request['videoLink'],request['startTime'], request['endTime'], OUTPUT_DIR)

    # We return the url where all images are and the image name to find it.
    return ROOT_URL+toReturn

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)