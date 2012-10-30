#!/usr/bin/env python2.7

"""Ancient code-breaking game "Bulls and Cows"."""

from random import sample

from psycopg2 import connect

class User(object):
    def __init__(self, user):
        self.db = connect("dbname=d95msa704d8g84 host=ec2-23-21-170-190.compute-1.amazonaws.com port=5432 user=jnisjfuuxcjlke password=0Mo84lR_s0te6YKVdfgTmLj18F sslmode=require")
        self.db.autocommit = True
        self.user = user
        self.cur = self.db.cursor()
        self.cur.execute(
            'select current_game from users where phone_number = %s',
            (user,))
        data = self.cur.fetchone()
        if data:
            self.game = data[0]
        else:
            self.cur.execute('insert into users (phone_number) values (%s)',
                             (user,))
            self.game = None

    def get_game(self):
        game = Game(self)
        if self.game != game.id:
            self.cur.execute('update users set current_game = %s where phone_number = %s',
                             (game.id, self.user))
        return game

    def __del__(self):
        self.db.close()

class Game(object):
    def __init__(self, user):
        self.user = user
        self.cur = user.db.cursor()
        self.id = user.game
        if not self.id:
            self.newgame()
        else:
            self.cur.execute('select goal_code, move_count, last_move from games where id = %s',
                             (self.id,))
            self.goal, self.move, self.last = self.cur.fetchone()

    def __del__(self):
        self.cur.close()

    def newgame(self):
        self.goal = ''.join(chr(x) for x in sample(range(ord('0'), ord('9')), 4))
        self.move = 0
        self.last = None
        self.cur.execute('insert into games (goal_code) values (%s) returning id',
                         (self.goal,))
        self.id = self.cur.fetchone()[0]

    def command(self, move):
        method = getattr(self, 'do_' + move, None)
        if method:
            return method()
        elif move:
            return self.make_move(move)
        else:
            return self.do_help()

    def do_help(self):
        return "This is Bulls and Cows. I picked a 4 unique digits (0-9). You need to guess them, in order. Text me your guess, and I'll tell you how many bulls (right digit in the right place) and cows (a digit I have, in the wrong place) you got."

    def make_move(self, move):
        bulls, cows = self.checkmove(move)
        if move != self.last:
            self.move += 1
            self.cur.execute('insert into moves (game, move_count, move, bulls, cows) values (%s, %s, %s, %s, %s)',
                             (self.id, self.move, move, bulls, cows))
            self.cur.execute('update games set move_count=%s, last_move=%s where id=%s',
                             (self.move, move, self.id))
        if bulls == 4:
            return "You won in {} moves".format(self.move)
        else:
            return "Move {}: {} Bulls, {} Cows".format(self.move, bulls, cows)

    def checkmove(self, move):
        bulls = cows = 0
        for i, a in enumerate(''.join(move.split())):
            if a in self.goal:
                if a == self.goal[i]:
                    bulls += 1
                else:
                    cows += 1
        return bulls, cows

