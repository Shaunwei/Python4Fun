# higher priority are dequeued first
# same priority obey FIFO 
"""
PriorityQueue(): Creates a new empty unbounded priority queue.

BPriorityQueue( numLevels ): Creates a new empty bounded priority queue with priority levels in the range from 0 to numLevels - 1.

isEmpty(): Returns a boolean value indicating whether the queue is empty.8.3 Priority Queues

length (): Returns the number of items currently in the queue.

enqueue( item, priority ): Adds the given item to the queue by inserting it in the proper position based on the given priority. The priority value must be within the legal range when using a bounded priority queue.

dequeue():item with two items order. An Removes and returns the front item from the queue, which is the the highest priority. The associated priority value is discarded. If have the same priority, then those items are removed in a FIFO item cannot be dequeued from an empty queue.
"""

####
# Implementation of the unbounded Priority Queue ADT using a Python list
# with new items appended to the end

class PriorityQueue :
    def __init__(self):
        self._qList = list()
    
    def isEmpty(self):
        return len(self) == 0
    
    def __len__(self):
        return len(self._qList)
    
    def enqueue(self, item, priority):
        # Create a new instance of the storage class and append it to the list
        entry = _PriorityQEntry(item, priority)
        self._qList.append(entry)
        
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue"
        # Find the entry with the highest priority
        highest = self._qList[0].priority
        nodeIndex = 0
        for i in range(len(self)):
            # See if the ith entry contains a higher priority (smaller integer)
            if highest > self._qList[i].priority:
                highest = self._qList[i].priority
        # Remove the entry with the highest priority and return the item
                nodeIndex = i
        entry = self._qList.pop(nodeIndex)
        return entry



class _PriorityQEntry:
    def __init__( self, item, priority ):
        self.item = item
        self.priority = priority


if __name__ == "__main__":
    Q = PriorityQueue(  )
    Q.enqueue( "purple", 5 )
    Q.enqueue( "black", 1 )
    Q.enqueue( "orange", 3 )
    Q.enqueue( "white", 0 )
    Q.enqueue( "green", 1 )
    Q.enqueue( "yellow", 5 )
    while not Q.isEmpty():
        item = Q.dequeue()
        print( item.item, item.priority )
