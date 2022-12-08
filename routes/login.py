from flask import Flask, requests
from flask_login import (
    LoginManger,
    current_user,
    login_required,
    login_user,
    logout_user
)
from oauthlib.oauth2 import WebApplicationClient
from scripts.db import DB
import os

login_bp = Blueprint('login',__name__,template_folder = 'templates')

GOOGLE_CLIENT_ID = os.environ.get()

#hiekajdflkjas;lfjdklfj









# Use Google to Perform OAUTH2 Authetication
"""
Authentication
1. Who are you? Use Google API to verify this
2. Collect the Token Back
3. Save token in Session

Questions

"""

"""
Authorization
1. What do you have the right to do? Use google api for this
2. Use the session token to check if they are logged in
3. Make a wrapper method @login OR use a function checkLogin() that returns true or false if logged in
"""

"""
client id: 740722874972-8m2504ehfsriuha012a930nfn536i83d.apps.googleusercontent.com
client secret: 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


"""

if __name__ == "__main__":
    # Call your functions here