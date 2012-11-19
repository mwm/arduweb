import os

from flask import Flask, url_for, redirect, request, send_from_directory

app = Flask(__name__)

from pasture import User
from smtplib import SMTP

@app.route('/')
def help():
    return redirect(url_for('static', filename='help.html'))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'cow.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/mailed', methods=['POST'])
def mailmove():
    try:
        res = send_result(str(request.form['from']), str(request.form['subject']),
                          str(request.form['body-plain']))
    except Exception as e:
        res = "Failed: " + str(e)
    print res
    return res


moomail = 'outbound@bulls-and-cows.mailgun.org'
def send_result(to, subject, command):
    s = SMTP('smtp.mailgun.org', 587)
    s.login('postmaster@bulls-and-cows.mailgun.org', '8wvv9y0wpgx8')
    phone = subject.partition('(')[2].translate(None, ']-() ')
    reply = User(phone).command(command)
    msg = "From: {}\r\nTo: {}\r\n\r\n{}\r\n".format(moomail, to, reply)
    result = s.sendmail(moomail, [to, 'mwm@mired.org'], msg)
    s.quit()
    return "{}\n{}".format(msg, result)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0', port=port)
 
