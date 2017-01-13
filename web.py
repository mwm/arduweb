"""The web server, via flask."""

from makers import make_repo, make_arduboy_json
from games import repos as repositories

from flask import Flask, abort, redirect, url_for


app = Flask(__name__)

@app.route('/')
def hello_world():
    return """<html><head><title>mwm's arduboy placeholder</title></head>
              <body><p>You probably want <a href="/repo">the repo</a> or
              the <a href="/static/Tiny-1010.arduboy">arduboy file</a></p></body>"""

@app.route('/arduboy/<game>')
def arduboy(game):
    out = make_arduboy_json(game)
    if out is None:
        abort(404)
    return out

@app.route('/repos/<repo>')
def repos(repo):
    out = make_repo(repo)
    if out is None:
        abort(404)
    return make_repo(repo)

class do_repo_redirect(object):
    def __init__(self, repo):
        self.repo = repo

    def __call__(self):
        return redirect(url_for('repos', repo=self.repo))

for key in repositories.iterkeys():
    if not key.startswith('_'):
        app.add_url_rule('/' + key, key, do_repo_redirect(key))
