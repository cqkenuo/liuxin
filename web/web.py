from flask import Flask
import os
from datetime import timedelta
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.secret_key = os.urandom(64)
app.permanent_session_lifetime = timedelta(hours=6)
CSRFProtect(app)


@app.route('/')
def index():
    pass


if __name__ == '__main__':
    app.run(threaded=True, host='127.0.0.1', port='88', debug=True)
