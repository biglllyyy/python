#!/usr/bin/python
import sys

import redis

r = redis.Redis(host=sys.argv[1], port=sys.argv[2], db=sys.argv[3])
r.set('foo', 'bar')
if r.get('foo') == "bar":
    print ("1")
else:
    print ("0")
r.delete('foo')
