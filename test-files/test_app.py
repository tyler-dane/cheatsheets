import os
import sys

from flask import Flask, render_template, jsonify, request
from waitress import serve

import utils
import logging

from app_utils import AppUtils
from forms import SelectFormList, SelectForm

app = flask(__name__, template_folder='templates', static_folder='static')
app.config['secret_key'] = os.urandom(32)


# @app.route("/")
# def index():
#     select_form_list = SelectFormList()
#     select_form_list.select_entries = utils.get_select_entries()
#
#     context = {
#         "select_form_list": select_form_list,
#     }
#
#return render_template("index.html", **context)

@app.route("/")
def index():
    return render_template("index-v2.html")

@app.route("/hello")
def hello():
    return render_template("hello.html")


@snap.route("/jquery_demo")
def jquery_demo():
    return render_template("jquery-demo.html")


@app.route('/background_process')
def background_process():
    try:
        lang = request.args.get('proglang', 0, type=str)
        if lang.lower() == 'python':
            return jsonify(result='You are wise')
        else:
            return jsonify(result='Try again.')
    except Exception as e:
        return str(e)


@app.route('/test_mic_link')
def test_mic_link(): 
    try:
        print("testing mic link")
        return jsonify(result="Started recording!")
    except Exception as e:
        return str(e)

app.route('/ssl_test')
def ssl_test():
def ssl_test():
    return render_template("ssl_test.html")


def setup_app():
    logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s: %(levelname)s: %(name)s: %(message)s',
            handlers=[
                logging.FileHandler("new_app.log"),
                logging.StreamHandler(sys.stdout)
            ]
    )


def test_logger():
    logger=logging.getLogger()
    logger.info("some message [app.py]")
    print("some print msg [app.py]")
    app_utils = AppUtils()
    print("out of app utils")


if __name__ == "__main__":
    setup_app()
    test_logger()
    serve(app, host="demo.company.local", expose_tracebacks=True, port=5004)  # This works for all urls!
    # serve(app, host="localhost") # This works for basic setup!
    # serve(app, host="demo.company.local") # This works for basic setup, too!

    # serve(app, host="demo.company.local", url_scheme="https", expose_tracebacks=True)
    # serve(app, listen="demo.company.local:443")

    # Steals 443 port from Apache if including port here
    # serve(app, host="demo.company.local", port=4003, url_scheme="https", expose_tracebacks=True)
    # serve(app, host="demo.company.local", url_scheme="https", expose_tracebacks=True) #Testing, not working yet
    # serve(app, host="demo.company.local", port=443, url_scheme="https", expose_tracebacks=True) # Trouble getting to
    # work
    # demo.company.local:8080/hello does NOT work
    # https://demo.company.local does NOT work
    # serve(app, host="demo.company.local", url_scheme="https")  # Testing

    # app.run(debug=True)
    # app.run(port=80, debug=True)
    # serve(app, listen="demo.company.local:80")
    # serve(app, host="demo.company.local", port=5003)  # runs, but no redirect
    # serve(app, host="0.0.0.0", port=5003)  # doesnt run if apache is using same port
    # serve(app, host="localhost", port=80)
    # serve(app, host="localhost") # this was the one that worked originally, the mysteriously stopped
