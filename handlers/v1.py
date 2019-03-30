#!/usr/bin/env python3

from flask import Flask
from flask import Blueprint


v1 = Blueprint("v1", __name__, url_prefix="/v1")

@v1.route('/login')
def login():
    return "hello login"

@v1.route('/signup')
def signup():
    return "hello signup"