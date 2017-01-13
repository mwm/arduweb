"""Dicionaries describing the repos we provide.

The "repos" dictionary is a description of the repositories on this server.
The keys will be used as paths to the generated repository. Those names
are in /repos/<name>, and /<name> is redirected to that URL for backwards
compatibility. This means that repos can't be named "repos" or "static".

The repo_template dictionary will be used to initialize each repo
object. It currently sets the api-version and maintainer. These values
can be overridden in the repos dictionary entries.

The item_template dictionary will be used to initialize items in each
repo. It currently sets the author and model, which can be overridden
in the repos dictionary.

The 'hex' entry in each item will be expanded to a static URL for the
named file. The same will be done for the 'cover' entry. If there is
no 'cover' entry, then the hex file URL with a png extension will be
used.
"""

from os.path import splitext

from os.path import splitext
from flask import url_for
from simplejson import dumps

# Default values to use for a repository and item in a repository
repo_template = {'api-version': '0.5', 'maintainer': 'mwm@mired.org'}

repos = {'repo': {'repository': "Mike's Arduboy Repo",
                  'item_default': {'author': 'mwm', 'model': 'Production'},
                  'items': {'1010': {'hex': 'Tiny-1010.hex',
                                     'version': '0.96',
                                     'description': 'A 10x10 block puzzle game.'}}},
         'family': {'repository': "Mike's Family Repo",
                    'item_default': {'author': 'mwm',
                                     'model': 'Production',
                                     'cover': 'Tiny-1010.png',
                                     'version': '0.96',
                                     'description': 'A 1010 block puzzle game.'},
                    'items': {'1010 for Mom': {'hex': 'Tiny-1010-Mom.hex'},
                              '1010 for Alan': {'hex': 'Tiny-1010-Alan.hex'},
                              '1010 for Paul': {'hex': 'Tiny-1010-Paul.hex'}}}
}

def make_repo(name):
    out = repo_template.copy()
    out.update(repos[name])
    del out['item_default']

    out['items'] = []
    for item_name in repos[name]['items'].iterkeys():
        out['items'].append(make_item(name, item_name))

    return dumps(out)

def make_item(repo, item):
        out = repos[repo]['item_default'].copy()
        out.update(repos[repo]['items'][item])
        out['name'] = item

        if 'cover' not in out:
            out['cover'] = filename=splitext(out['hex'])[0] + '.png'
        out['cover'] = url_for('static', filename=out['cover'], _external=True)
        out['hex'] = url_for('static', filename=out['hex'], _external=True)
        return out
