"""Tools to make output values"""

from games import games, repos

from flask import escape, url_for

from os.path import join, splitext
from cStringIO import StringIO
from zipfile import ZipFile
from simplejson import dumps


def make_zipfile(game):
    """Create a .arduboy file in a StringIO file"""

    outfile = StringIO()
    zf = ZipFile(outfile, 'w')
    info = make_arduboy(game)
    zf.writestr('info.json', dumps(info))

    for hf in info['hexes']:
        hexfile = hf['hex']
        zf.write(join('static', hexfile), hexfile)

    for img in info['screenshots']:
        zf.write(join('static', img), img)

    if 'banner' in info:
        zf.write(join('static', info['banner']), info['banner'])

    zf.close()
    out = outfile.getvalue()
    outfile.close()
    return out

def make_arduboy(game):
    """Create an arduboy dictionary from an entry in the games dictionary."""

    out = make_new(games, game)
    if out is None:
        return None
    if 'title' not in out:
        out['title'] = game

    # Pluralize hex files and screenshots
    if 'hexes' not in out:
        out['hexes'] = [{'title': game, 'hex': out['hex']}]
    if 'screenshots' not in out:
        if 'cover' in out:
            out['screenshots'] = [out['cover']]
        else:
            out['screenshots'] = [splitext(hex['hex'])[0] + '.png'
                                  for hex in out['hexes']]

    return out


def make_html(name, repo):
    """Create an HTML description of a repository."""

    desc = escape(repo['repository'])
    out = ["<html><head><title>%s</title></head><body></h1>%s</h1>"
           % (desc, desc)]
    
    out.append("<p>Maintained by %s.</p><dl>" % escape(repo['maintainer']))
    for game in repo['items']:
        out.append("<dt>%s (%s)</dt><dd>"
                   % (escape(game['name']), escape(game['version'])))
        if 'cover' in game:
            out.append('<img src="%s" style="float:left">' % escape(game['cover']))
        out.append("<p>%s</p>" % escape(game['description']))
        out.append('<p><a href="%s">Hex</a> <a href="%s">Arduboy file</a>'
                   % (escape(game['hex']),
                      url_for('arduboy', game='%s.arduboy' % game['name'])))
        out.append("</dd>")
    out.append('</dl><p><a href="%s">for Ardumate</a></body></html>'
               % url_for('repos', repo=name + '.json'))
    return '\n'.join(out)

def make_repo(name):
    """Make a dictionary for a repository."""
    
    out = make_new(repos, name)
    if out is None:
        return None
    items = out['items']

    out['items'] = []
    for item in items:
        out['items'].append(make_entry(item))

    return out

def make_entry(item):
    """Make a dictionary for an ardumate repo entry."""

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

    return out


def make_new(data, name):
    """Make a copy of a dictionary with defaults."""

    if name not in data:
        return None
    out = data['_defaults'].copy()
    out.update(data[name])
    return out
    
