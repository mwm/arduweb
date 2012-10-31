#!/usr/bin/env python2.7

"""Ancient code-breaking game "Bulls and Cows"."""

from random import sample
from string import digits

from psycopg2 import connect

class User(object):
    def __init__(self, user):
        self.db = connect("dbname=d95msa704d8g84 host=ec2-23-21-170-190.compute-1.amazonaws.com port=5432 user=jnisjfuuxcjlke password=0Mo84lR_s0te6YKVdfgTmLj18F sslmode=require")
        self.db.autocommit = True
        self.user = user
        self.cur = self.db.cursor()
        self.cur.execute('select current_game from users where phone_number = %s',
                         (user,))
        data = self.cur.fetchone()
        if data:
            self.game = data[0]
        else:
            self.cur.execute('insert into users (phone_number) values (%s)',
                             (user,))
            self.game = None

    def __del__(self):
        self.db.close()

    def command(self, move):
        method = getattr(self, 'do_' + move.lower(), None)
        if method:
            return method()
        elif move:
            return self.make_move(''.join(move.split()))
        else:
            return self.do_help()

    def do_help(self):
        """Provide a help message."""

        return "This is the game Bulls and Cows. See http://moo.mired.org/ for instructions on how to play. Text 'commands' for a list of commands."

    def do_commands(self):
        "Provide a list of commands."

        commands = [m[3:] for m in dir(self) if m.startswith('do_')]
        return '\n'.join('{0:10}{1}'.format(m, getattr(self, 'do_' + m).__doc__)
                         for m in commands)

    def do_new(self):
        """Start a new game."""

        self.game = None
        self.get_game()
        return "Started a new game."
    
    do_start = do_new

    def make_move(self, move):
        game = self.get_game()
        if move != game.last == game.goal:
            # We won it last move, start a new game
            self.game = None
            return self.get_game().move(move)
        return game.move(move)

    def get_game(self):
        game = Game(self)
        if self.game != game.id:
            self.game = game.id
            self.cur.execute('update users set current_game = %s where phone_number = %s',
                             (game.id, self.user))
        return game


class Game(object):
    def __init__(self, user):
        self.cur = user.db.cursor()
        self.id = user.game
        if not self.id:
            self.newgame()
        else:
            self.cur.execute('select goal_code, move_count, last_move from games where id = %s',
                             (self.id,))
            self.goal, self.moves, self.last = self.cur.fetchone()

    def __del__(self):
        self.cur.close()

    def newgame(self):
        self.goal = ''.join(sample(digits, 4))
        self.moves = 0
        self.last = None
        self.cur.execute('insert into games (goal_code) values (%s) returning id',
                         (self.goal,))
        self.id = self.cur.fetchone()[0]

    def move(self, move):
        if (len(move) != 4 or len(set(move)) != 4 or
              any((x not in digits) for x in move)):
            return 'Invalid move.'

        bulls, cows = self.checkmove(move)
        if move != self.last:
            self.moves += 1
            self.cur.execute('insert into moves (game, move_count, move, bulls, cows) values (%s, %s, %s, %s, %s)',
                             (self.id, self.moves, move, bulls, cows))
            self.cur.execute('update games set move_count=%s, last_move=%s where id=%s',
                             (self.moves, move, self.id))
        if bulls == 4:
            return "You won in {} moves".format(self.moves)
        else:
            return "Move {}: {} Bulls, {} Cows".format(self.moves, bulls, cows)

    def checkmove(self, move):
        bulls = cows = 0
        for i, a in enumerate(''.join(move.split())):
            if a in self.goal:
                if a == self.goal[i]:
                    bulls += 1
                else:
                    cows += 1
        return bulls, cows

