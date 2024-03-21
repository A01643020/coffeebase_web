import os
import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv

load_dotenv()

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(credentials.ApplicationDefault() ,options={
    'databaseURL': os.getenv('FIREBASE_DATABASE_URL'),
})

keys = ["Led", "POT"]

def obtenerDatos():
    db_path = "/"
    try:
        ref = db.reference(db_path)
        response = ref.get()
        output = {}
        for key in keys:
            output[key] = response.get(key, None)
        return output
        
    except Exception as e:
        print(f"Failed to get values: {e}")
        return {}