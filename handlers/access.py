#!/usr/bin/env python3

from flask import Blueprint
from flask_httpauth import HTTPBasicAuth


access = Blueprint("user", __name__, url_prefix="/access")
auth = HTTPBasicAuth()

id_list = {
    "Tanaka": "1111",
    "Suzuki": "1234"
}

@access.route('/login')
@auth.login_required
def login():
    return "hello login"

@auth.get_password
def get_password(id):
    if id in id_list:
        return id_list.get(id)
    return None

@access.route('/signup')
def signup():
    return "hello signup"
