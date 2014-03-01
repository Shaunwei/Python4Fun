# doubly linked list
class DLinkList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def isEmpty(self):
        return self._size == 0
    
    def __len__(self):
        return self._size
    
    def prepend(self, entry):
        node = _DListNode(entry)
        node.next = self._head
        
        if len(self) == 0:
            self._tail = node
        else:
            self._head.prev = node

        self._head = node
        self._size += 1
      
    def append(self, entry):
        node = _DListNode(entry)
        if len(self) == 0:
            self._head = node
        else:
            self._tail.next = node
            node.prev = self._tail

        self._tail = node
        self._size += 1
        
    def traversal(self):
        assert not self.isEmpty(), "Cannot traversal from empty list"
        curNode = self._head
        while curNode.next is not None:
            print(curNode.data)
            curNode = curNode.next
        print(curNode.data)
        
    def revTraversal(self):
        assert not self.isEmpty(), "Cannot traversal from empty list"
        curNode = self._tail
        while curNode.prev is not None:
            print(curNode.data)
            curNode = curNode.prev
        print(curNode.data)

class _DListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None



if __name__=="__main__":
    L = DLinkList()
    L.prepend(21)
    L.append(37)
    L.prepend(13)
    L.append(58)
    L.append(74)
    print("traver")
    L.traversal()
    print("revOrder")
    L.revTraversal()
