from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return ('Arduboy stuff at ' + url_for('static', filename='repo.json') + '\n'
            + url_for('static', filename='image.png') + '\n'
            + url_for('static', filename='Tiny-1010.hex'))
