#!/usr/bin/env python2.7

"""Ancient code-breaking game "Bulls and Cows"."""

from random import sample

class Game(object):
    def __init__(self):
        self.goal = ''.join(chr(x) for x in sample(range(ord('0'), ord('9')), 4))
        self.move = 0

    def checkmove(self, move):
        bulls = cows = 0
        for i, a in enumerate(''.join(move.split())):
            if a in self.goal:
                if a == self.goal[i]:
                    bulls += 1
                else:
                    cows += 1
        self.move += 1
        return self.move, bulls, cows

