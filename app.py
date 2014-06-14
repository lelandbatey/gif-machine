from __future__ import print_function
from flask import Flask, request, json, render_template
from subprocess import call
from pprint import pprint
import os
import gifMachine
import random
import base64
import flask
import json
import sys

app = Flask(__name__)

# Configuration for running gifMachine.
ROOT_URL = "http://public_URI_for_img_folder/"
OUTPUT_DIR = "directory_on_filesystem_where_images_go"


# If there's a config file, we use that for our settings
if os.path.isfile('gm_config.json'):
    jf = open('gm_config.json','r')
    config     = json.loads(jf.read())
    ROOT_URL   = config['ROOT_URL']
    OUTPUT_DIR = confif['OUTPUT_DIR']
    jf.close()


app.debug = True

@app.route('/')
def root():
    return render_template("frontpage.html")

@app.route('/makegif', methods = ['POST'])
def make_gif():
    print("Whooo, we are recieving the thing!")
    toReturn = ''

    # Takes the post request and calls the build_gif params of gifMachine
    if request.json:
        print("the request is json")
        print(request.form)
        toReturn = gifMachine.build_gif(base64.b64decode(request.json['videoLink']),\
            request.json['startTime'], request.json['endTime'], OUTPUT_DIR,\
            request.json['width'])
    # Why are we decoding a base64 string here? Well, to get around the problem
    # of dealing with escaping url's and such, they're just encoded in base64 by
    # the browser, then decoded on this end.

    else:
        print("The request is NOT json")
        print(request.form)
        print(request.data)
    
    returnDict = {"imgAddress": str(ROOT_URL+toReturn)}

    toReturn = json.dumps(returnDict)

    # response = flask.make_response(ROOT_URL+toReturn)
    # response.headers["Content-type"] = "text/plain"

    print(toReturn)

    # We return the url where all images are and the image name to find it.
    return toReturn

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)