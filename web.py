from flask import Flask, url_for, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return """<html><head><title>mwm's arduboy placeholder</title></head>
              <body><p>You probably want <a href="/repo">the repo</a></p></body>"""

@app.route('/repo')
def repo():
    return redirect(url_for('static', filename='repo.json'))

@app.route('/family')
def family():
    return redirect(url_for('static', filename='family.json'))
