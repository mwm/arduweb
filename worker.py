#!/usr/bin/env python

"""The text player app - gets moves from rq and texts the results back."""

from os import getenv

import redis
from rq import Worker, Queue, Connection


# Preload the game
import pasture

conn = redis.from_url(getenv('REDISTTOGO_URL', 'redis://localhost:6379'))
with Connection(conn):
    Worker(map(Queue, ('high', 'default', 'low'))).work()
