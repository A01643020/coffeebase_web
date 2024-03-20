import pyrebase
import os
from dotenv import load_dotenv

load_dotenv()

firebase_config = {
    "apiKey": os.getenv('FIREBASE_API_KEY'),
    "authDomain": os.getenv('FIREBASE_AUTH_DOMAIN'),
    "databaseURL": os.getenv('FIREBASE_DATABASE_URL'),
}

pyrebase_app = pyrebase.initialize_app(firebase_config)
firebase_database = pyrebase_app.database()

def obtenerDatos():
    db_path = "/"
    try:
        response = firebase_database.child(db_path).get()
        if response:
            result = response.val()
            led = result.get("LED", None)
            temp = result.get("Temperature", None)
            return led, temp
        
    except Exception as e:
        print(f"Failed to get values: {e}")
        return None, None