# -*- coding: utf-8 -*-
from flask import Flask, request
from api.user import *
from api.poclist import *
from api.task import *

from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.register_blueprint(userbp)
app.register_blueprint(taskbp)
app.register_blueprint(pocbp)


@app.route('/api')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


if __name__ == '__main__':
    app.run(debug=True)
