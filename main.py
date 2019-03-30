#!/usr/bin/env python3

from flask import Flask
from handlers.access import access

app = Flask(__name__)
app.config['SECRET_KEY']

#グルーピングを登録
app.register_blueprint(access)

if __name__ == '__main__':
    app.run(debug=True)


