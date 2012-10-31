import os
from sys import stdout

from flask import Flask, url_for, redirect, request, send_from_directory

app = Flask(__name__)

from pasture import User

@app.route('/')
def help():
    return redirect(url_for('static', filename='help.html'))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'cow.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/<user>/<command>')
def move(user, command):
    """Quick hack for testing moves."""
    return User(user).command(command)

@app.route('/mailed', methods=['POST'])
def mailmove():
    subject = str(request.form['subject'])
    command = request.form['body-plain']
    phone = subject.partition('[')[2].partition(']')[0].translate(None, '()- ')
    phone = str(phone).translate(None, '-() ')
    return move(phone, command)	# Not sure where this goes...

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0', port=port)
 
