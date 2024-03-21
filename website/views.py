from flask import jsonify, render_template, request, Blueprint

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

@views.route('/api/power', methods=['POST'])
def power():
    data = request.get_json()
    firebase.database.update({
        "Led": data["power"]
    })
    return jsonify({"message": "LED state updated successfully"}), 200
