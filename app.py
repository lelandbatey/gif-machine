from __future__ import print_function
from flask import Flask, request, json, render_template
from pprint import pprint
import gif_machine
import base64
import json
import os


APP = Flask(__name__)

# Configuration for running gifMachine.
ROOT_URL = "http://public_URI_for_img_folder/"
OUTPUT_DIR = "directory_on_filesystem_where_images_go"

# If there's a config file, we use that for our settings
if os.path.isfile('gm_config.json'):
    JSON_FILE = open('gm_config.json', 'r')
    CONFIG = json.loads(JSON_FILE.read())
    ROOT_URL = CONFIG['ROOT_URL']
    OUTPUT_DIR = CONFIG['OUTPUT_DIR']
    JSON_FILE.close()

APP.debug = True

@APP.route('/')
def root():
    """Just renders the frontpage."""
    return render_template("frontpage.html")

@APP.route('/makegif', methods=['POST'])
def make_gif():
    """Makes the gif, returning the url for the gif."""
    print("Whooo, we are recieving the thing!")
    to_return = ''

    # Takes the post request and calls the build_gif params of gifMachine
    if request.json:
        print("the request is json")
        print(request.form)
        to_return = gif_machine.build_gif(
            base64.b64decode(request.json['videoLink']),
            request.json['startTime'], request.json['endTime'], OUTPUT_DIR,
            request.json['width'])
    # Why are we decoding a base64 string here? Well, to get around the problem
    # of dealing with escaping url's and such, they're just encoded in base64 by
    # the browser, then decoded on this end.

    else:
        print("The request is NOT json")
        print(request.form)
        print(request.data)
    
    return_dictionary = {"imgAddress": str(ROOT_URL+to_return)}
    to_return = json.dumps(return_dictionary)

    # response = flask.make_response(ROOT_URL+to_return)
    # response.headers["Content-type"] = "text/plain"

    print(to_return)

    # We return the url where all images are and the image name to find it.
    return to_return

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    PORT = int(os.environ.get('PORT', 5000))
    APP.debug = True
    APP.run(host='0.0.0.0', port=PORT)
