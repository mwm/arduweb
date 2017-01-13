"""Tools to create json strings and zip files"""

from games import games, repos

from flask import url_for
from simplejson import dumps

from os.path import splitext

def make_repo(name):
    """Create a json string from an entry in the repos dictionary."""
    
    out = make_new(repos, name)
    if out is None:
        return None
    items = out['items']

    out['items'] = []
    for item in items:
        out['items'].append(make_item(item))

    return dumps(out)

def make_item(item):
    """Create an ardumate json string from item in the games dictionary."""

    out = make_new(games, item)
    if out is None:
        return None

    if 'name' not in out:
        out['name'] = item

    # Possibly create a cover image.
    if 'cover' not in out:
        out['cover'] = splitext(out['hex'])[0] + '.png'

    out['cover'] = url_for('static', filename=out['cover'], _external=True)
    out['hex'] = url_for('static', filename=out['hex'], _external=True)

    return dumps(out)

def make_arduboy_json(game):
    """Create an arduboy json string from an entry in the games dictionary."""

    out = make_new(games, game)
    if out is None:
        return None
    if 'title' not in out:
        out['title'] = game

    # Pluralize hex files and screenshots
    if 'hexes' not in out:
        out['hexes'] = [out['hex']]
    if 'screenshots' not in out:
        if 'cover' in out:
            out['screenshots'] = [out['cover']]
        else:
            out['screenshots'] = [splitext(hex)[0] + '.png'
                                  for hex in out['hexes']]

    return dumps(out)

def make_new(dict, name):
    """Fix the URL's in a game dictionary."""

    if name not in dict:
        return None
    out = dict['_defaults'].copy()
    out.update(dict[name])
    return out
    
