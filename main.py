#!/usr/bin/env python3

from flask import Flask
from handlers.v1 import v1

app = Flask(__name__)

#グルーピングを登録
app.register_blueprint(v1)

if __name__ == '__main__':
    app.run(debug=True)


