import os
from flask import Flask, url_for, redirect

app = Flask(__name__)

from pasture import User

@app.route('/')
def help():
    return redirect(url_for('static', filename='help.html'))

@app.route('/<user>/<command>')
def move(user, command):
    return User(user).command(command)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0', port=port)
 
