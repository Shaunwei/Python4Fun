#!/usr/bin/env python
from pylistqueue import Queue


q = Queue()
print "enqueue 28 19 45"
q.enqueue( 28 )
q.enqueue( 19 )
q.enqueue( 45 )
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
