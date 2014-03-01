# Implementation of the bounded Priority Queue ADT using an array of
# queue in which the queue are implemented using a linked list
from array import Array
from llistqueue import Queue

class BPriorityQueue:
    def __init__(self, numLevels):
        self._qSize = 0
        self._qLevels = Array(numLevels)
        for i in range(numLevels):
            self._qLevels[i] = Queue
    
    # Returns True if queue is empty
    def isEmpty( self ):
        return len(self) == 0
    
    def __len__(self):
        return self._qSize
    
    # Adds item with priority to proper location
    def enqueue( self, item, priority ):
        assert priority >= 0 and priority <= len(self._qLevels),\
               "Invaid priority level."
        self._qLevels[priority].enqueue(item, priority)
    
    # Removes and returns the next item in the queue
    def dequeue( self ):
        # Make sure the queue is not empty
        assert not self.isEmpty(), "Cannot dequeue from an empty queue"
        # Find the first non-empty queue
        i = 0
        p = len(self._qLevels)
        while i < p and not self._qLevels[i].isEmpty():
            i += 1
            # We know the queue is not empty, so dequeue from the ith queue
            return self._qLevels[i].dequeue()
        


if __name__ == "__main__":
    Q = BPriorityQueue( 6 )
    Q.enqueue( "purple", 5 )
    Q.enqueue( "black", 1 )
    Q.enqueue( "orange", 3 )
    Q.enqueue( "white", 0 )
    Q.enqueue( "green", 1 )
    Q.enqueue( "yellow", 5 )
    while not Q.isEmpty():
        item = Q.dequeue()
        print( item )
