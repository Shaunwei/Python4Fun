class LPriorityQueue:
    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._count = 0
        
    def isEmpty(self):
        return self._count == 0
    
    def __len__(self):
        return self._count
    
    def enqueue(self, item, priority):
        node = _LPriorityNode(item, priority)
        if self.isEmpty():
            self._qhead = node
        else:
            self._qtail.next = node

        self._qtail = node
        self._count += 1

    # Removes the entry with the highest priority
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue"
        curHighNode = self._qhead
        befHighNode = None
        highest = curHighNode.priority
        curNode = self._qhead
        preNode = None
        while curNode.next is not None:
            # search the node with the highest priority( smaller integer ) 
            if curNode.priority < highest:
                befHighNode = preNode
                curHighNode = curNode
                highest = curNode.priority
            else:
                preNode = curNode
                curNode = curNode.next
        # Removes the Highest Node
        
        # empty the Queue if dequeue the last item
        if self._qhead == self._qtail:
            node = self._qhead
            self._count = 0
            self._qhead = self._qtail = None
            return node

        # If the node is the head move the qhead to the next
        # if the node is the tail move the qtail to the bef
        if curHighNode == self._qhead:
            self._qhead = curHighNode.next
        elif curHighNode == self._qtail:
            self._qtail = befHighNode
            befHighNode.next = None
        else:
            befHighNode.next = curHighNode.next
        self._count -= 1
        return curHighNode

class _LPriorityNode(object):
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
        self.next = None

if __name__ == "__main__":
    Q = LPriorityQueue(  )
    Q.enqueue( "purple", 5 )
    Q.enqueue( "black", 1 )
    Q.enqueue( "orange", 3 )
    Q.enqueue( "white", 0 )
    Q.enqueue( "green", 1 )
    Q.enqueue( "yellow", 5 )
    while not Q.isEmpty():
        item = Q.dequeue()
        print( item.item, item.priority )
