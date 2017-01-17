"""Dicionaries describing the games and repos we provide.

The "repos" dictionary is a description of the repositories on this server.  The
keys will be used as paths to the generated repository. Those names
show up as either json files for ardumate or html pages in in
/repos/<name>, and /<name> is redirected to the json file for
backwards compatibility. It's expected there won't be many repos per
server, and the names"repos", "arduboy" and "static" are unusable.

The "games" dictionary is a description of the games we provide. The entries are
for either ardumate json files or arduboy info.json files. A number of
entries will be generated automatically if they are not present:

   - name (ardumate)/title (arduboy): from key for that entry in the dictionary.
   - hex (ardumate)/hexes (arduboy): from the name (ardumate) or title (arduboy)
   - cover (ardumate): from the name entry
   - screenshots (arduboy): from the cover or hexes entry

The "_defaults" entry in each dictionary provides default entries for each.
These can be used for values common to all or most entries, and overridden
in each individual entry.

Any static files - meaning hex or image files - should be saved in
the "static" directory. The web front end will try and serve them from there.
"""

repos = {'_defaults': {'api-version': '0.5', 'maintainer': 'mwm@mired.org'},
         'repo': {'repository': "Mike's Arduboy Repo",
                  'items': ['1010']},
         'family': {'repository': "Mike's Family Repo",
                    'items': ['1010 for Mom', '1010 for Alan', '1010 for Paul']}}

games = {'_defaults': {'author': 'mwm', 'model': 'Production',
                       'device': 'Arduboy', 'banner': 'banner.png'},
         '1010': {'hex': 'Tiny-1010.hex',
                  'version': '0.96',
                  'description': 'A 10x10 block puzzle game.'},
         '1010 for Mom': {'hex': 'Tiny-1010-Mom.hex',
                          'cover': 'Tiny-1010.png',
                          'version': '0.96',
                          'description': 'A 10x10 block puzzle game.'},
         '1010 for Alan': {'hex': 'Tiny-1010-Alan.hex',
                           'cover': 'Tiny-1010.png',
                           'version': '0.96',
                           'description': 'A 10x10 block puzzle game.'},
         '1010 for Paul': {'hex': 'Tiny-1010-Paul.hex',
                           'cover': 'Tiny-1010.png',
                           'version': '0.96',
                           'description': 'A 10x10 block puzzle game.'},
         }
