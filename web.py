from flask import Flask, abort, redirect, url_for

from repos import repos as repositories, make_repo, dumps

app = Flask(__name__)


@app.route('/')
def hello_world():
    return """<html><head><title>mwm's arduboy placeholder</title></head>
              <body><p>You probably want <a href="/repo">the repo</a> or
              the <a href="/static/Tiny-1010.arduboy">arduboy file</a></p></body>"""

@app.route('/repos/<repo>')
def repos(repo):
    if repo in repositories:
        return make_repo(repo)
    else:
        abort(404)

class do_repo_redirect(object):
    def __init__(self, repo):
        self.repo = repo

    def __call__(self):
        return redirect(url_for('repos', repo=self.repo))

for key in repositories.iterkeys():
    app.add_url_rule('/' + key, key, do_repo_redirect(key))
