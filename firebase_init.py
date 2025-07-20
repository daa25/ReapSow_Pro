import os
import firebase_admin
from firebase_admin import credentials

def initialize_firebase():
    try:
        cred_json = os.getenv("FIREBASE_CREDENTIALS_JSON")
        if not cred_json:
            raise ValueError("Missing FIREBASE_CREDENTIALS_JSON env variable.")
        cred = credentials.Certificate(eval(cred_json))
        firebase_admin.initialize_app(cred)
        return True
    except Exception as e:
        print(f"Firebase init error: {e}")
        return False
