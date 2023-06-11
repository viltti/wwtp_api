from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash, generate_password_hash
from flask import current_app

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    correct_username = current_app.config['BASIC_AUTH_USERNAME']
    correct_password = current_app.config['BASIC_AUTH_PASSWORD']
    if username == correct_username and check_password_hash(generate_password_hash(correct_password), password):
        return username