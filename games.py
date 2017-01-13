"""Dicionaries describing the games and repos we provide.

The "repos" dictionary is a description of the repositories on this server.
The keys will be used as paths to the generated repository. Those names
are in /repos/<name>, and /<name> is redirected to that URL for backwards
compatibility. It's expected there won't be many repos per server, and the names
"repos", "arduboy" and "static" are unusable.

The "games" dictionary is a description of the games we provide.

The "_defaults" entry in each dictionary provides default entries for each.
These can be used for values common to all or most entries, and overridden
in each individual entry.

Any static files - meaning hex or image files - should be saved in
the "static" directory. The web front end will try and serve them from there,
and the cli front end (if I ever write one) will serve them from there.
"""

repos = {'_defaults': {'api-version': '0.5', 'maintainer': 'mwm@mired.org'},
         'repo': {'repository': "Mike's Arduboy Repo",
                  'items': ['1010']},
         'family': {'repository': "Mike's Family Repo",
                    'items': ['1010 for Mom', '1010 for Alan', '1010 for Paul']}}

games = {'_defaults': {'author': 'mwm', 'model': 'Production',
                           'device': 'Arduboy'},
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
