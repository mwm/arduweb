"""The web server, via flask."""

from games import repos as repositories
from makers import make_html, make_repo, make_zipfile

from flask import Flask, abort, redirect, url_for

from simplejson import dumps

app = Flask(__name__)

@app.route('/')
def hello_world():
    repos = [key for key in repositories.iterkeys() if not key.startswith('_')]
    if len(repos) == 1:
        return redirect(url_for('repos', repo=repos[0] + '.html'))
    out = ["<html><head><title>Arduboy repos</title></head><body>"]
    out.append('<h1>Arduboy repositories hosted here</h1>')
    for repo in repos:
        out.append('<li><a href="%s">%s</a></li>'
                   % (url_for('repos', repo=repo + '.html'), repo))
    out.append('</ul></body></html>')
    return '\n'.join(out)


@app.route('/arduboy/<game>')
def arduboy(game):
    if game.endswith('.arduboy'):
        game = game[:-8]
    elif game.endswith('.zip'):
        game = game[:-4]
    out = make_zipfile(game)
    if out is None:
        abort(404)
    return out


@app.route('/repos/<repo>')
def repos(repo):
    out = make_repo(repo[:-5] if '.' in repo else repo)
    if out is None:
        abort(404)
    if repo.endswith('.html'):
        return make_html(repo[:-5], out)
    return dumps(out)

# Install the backwards compatible repo redirects
class do_repo_redirect(object):
    def __init__(self, repo):
        self.repo = repo

    def __call__(self):
        return redirect(url_for('repos', repo=self.repo + '.json'))

for key in repositories.iterkeys():
    if not key.startswith('_'):
        app.add_url_rule('/' + key, key, do_repo_redirect(key))
