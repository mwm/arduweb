#!/usr/bin/env python

"""The text player app - gets moves from rq and texts the results back."""

import redis
from rq import worker, Queue, Connection

# Preload the game
import pasture

conn = redis.from_url(os.getenv('REDISTTOGO_URL', 'redis://localhost:6379'))
with Connection(conn):
    Worker(map(Queue, ('high', 'default', 'low'))).work()
