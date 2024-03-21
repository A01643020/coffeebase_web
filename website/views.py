from flask import jsonify, render_template,  redirect, url_for, session, Blueprint

import schedule
import time

from . import firebase
    
views = Blueprint('views', __name__)


@views.route('/', methods=['POST', 'GET'])
def home():
    data = firebase.obtenerDatos()
    return render_template("base.html", data = data)

@views.route('/api/data', methods=['GET'])
def get_data():
    return firebase.obtenerDatos()
