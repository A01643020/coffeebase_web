from flask import jsonify, render_template,  redirect, url_for, session, Blueprint

import schedule
import time

from . import firebase
    
views = Blueprint('views', __name__)

def show_from_database():
    new_data = firebase.obtenerDatos()
    print(new_data)

schedule.every(3).seconds.do(show_from_database)

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

import threading

threading.Thread(target=run_schedule).start()


@views.route('/')
def home():
    return render_template("base.html") #, temperatura = temperatura, distancia = distancia)