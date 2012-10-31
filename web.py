import os

from flask import Flask, url_for, redirect, request, send_from_directory

app = Flask(__name__)

from pasture import User
from googlevoice.voice import Voice

@app.route('/')
def help():
    return redirect(url_for('static', filename='help.html'))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'cow.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/mailed', methods=['POST'])
def mailmove():
    return send_result(str(request.form['subject']), request.form['body-plain'])

def send_result(subject, command):
    phone = subject.partition('(')[2].translate(None, ']-() ')
    v = Voice()
    v.login('mike.w.meyer@gmail.com', "_Pdn&Z4Gye'~yCP9]bMH%-@M'")
    result = User(phone).command(command)
    v.send_sms(phone, result)
    return result

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0', port=port)
 
