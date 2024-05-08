import os.path
import sys
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google.oauth2 import id_token
import jwt

SCOPES =["https://www.googleapis.com/auth/userinfo.email",
         "openid",
         "https://www.googleapis.com/auth/userinfo.profile"]

def request_creds():
    creds = None
    if os.path.exists("creds.json"):
        flow = InstalledAppFlow.from_client_secrets_file(
            "creds.json", 
            SCOPES)
        creds = flow.run_local_server(port=0)
        token_id = creds.id_token
        with open("token.json", "w") as token:
            token.write(creds.to_json())
        print(token_id)
        a = Credentials.from_authorized_user_file("token.json", SCOPES)
        return creds.to_json()
    else:
        print("Credentials not Avalible")
    sys.exit(1)

def get_creds():
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        return creds
    return request_creds()

def decode_google_oauth_token(token):
    try:
        # Specify the client ID of your application
        CLIENT_ID = '592133786316-k0nn6ltbc74c20ojje96nrqbqeebc1sd.apps.googleusercontent.com'

        # Verify the token
        idinfo = id_token.verify_oauth2_token(token, Request(), CLIENT_ID)

        # Extract user information
        user_id = idinfo['sub']
        email = idinfo.get('email')

        return user_id, email
    except ValueError as e:
        # Token is invalid
        print("Invalid token:", e)
        return None, None
