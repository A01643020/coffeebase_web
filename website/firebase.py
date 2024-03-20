import os
import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv

load_dotenv()

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(credentials.ApplicationDefault() ,options={
    'databaseURL': os.getenv('FIREBASE_DATABASE_URL'),
})

def obtenerDatos():
    db_path = "/"
    try:
        ref = db.reference(db_path)
        response = ref.get()
        if response:
            led = response.get("Led", None)
            temp = response.get("POT", None)
            return led, temp
        
    except Exception as e:
        print(f"Failed to get values: {e}")
        return None, None