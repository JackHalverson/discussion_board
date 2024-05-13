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
        return Credentials.from_authorized_user_file("token.json", SCOPES)
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

