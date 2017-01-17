#!/usr/bin/env python

"""A simple cli interface to create arduboy zip files."""

from makers import make_zipfile

from sys import argv

def make_arduboy(name):
    out = open(name + '.arduboy', 'w')
    out.write(make_zipfile(name))
    out.close()

if __name__ == '__main__':
    for name in argv[1:]:
        make_arduboy(name)
