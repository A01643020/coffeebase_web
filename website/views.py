from flask import jsonify, render_template,  redirect, url_for, session, Blueprint

import schedule
import time

from . import firebase
    
views = Blueprint('views', __name__)

led, pot = firebase.obtenerDatos()


@views.route('/')
def home():
    return render_template("base.html", led = led, pot = pot) #, temperatura = temperatura, distancia = distancia)