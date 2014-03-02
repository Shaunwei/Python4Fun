# doubly linked list
class DLinkList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        self._probe = None
        
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
        

    # four cases:
        # if the list is empty
        # add the node to the front
        # add the node to the bottom
        # add the node to the middle
    def insert(self, entry):
        node = _DListNode(entry)

        if self._head == None:
            self._head = node
            self._tail = node
        # if new node is less than head note do prepend
        elif node.data < self._head.data:
            self.prepend(entry)
        # if new node is larger than tail note do append
        elif node.data > self._tail.data:
            self.append(entry)
        else:
            # node is somewhere in the mid
            curNode = self._head
            while curNode.data < node.data and curNode is not None:
                curNode = curNode.next
            else:
                node.prev = curNode.prev
                node.next = curNode
                curNode.prev.next = node
                curNode.prev = node
    
    def remove(self, target):
        node = _DListNode(target)
        assert not self.isEmpty(),"Cannot remove data from empty list" 
        assert self.probing(target), "Node must exist in the list."
        if node.data == self._head.data:
            if self._probe == self._head:
                self._probe == None
            else: 
                pass
            self._head.next.prev = None
            self._head = self._head.next
        elif node.data == self._tail.data:
            if self._probe == self._tail:
                self._probe == None
            else:
                pass
            self._tail.prev.next = None
            self._tail = self._tail.prev
        else:
            curNode = self._head
            while curNode is not None and curNode.data <= node.data:
                if curNode.data == node.data:
                    curNode.prev.next = curNode.next
                    curNode.next.prev = curNode.prev
                    node.prev = None
                    node.next = None
                    return node
                else:
                    curNode = curNode.next
            
            
        
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

    # Given the head, tail and the probe references, probe the list for a target
        
    # Make sure the list is not empty
    def probing(self, target):
        if self._head is None:
            return False
        elif self._probe is None:
            self._probe = self._head
            
        # If the target comes before the probe node, we traverse backward
        # otherwise traverse forward
        # If the target is found in the list, return True
        # otherwise return False
        if target < self._probe.data:
            while self._probe is not None and target <= self._probe.data:
                if target == self._probe.data:
                    return True
                else:
                    self._probe = self._probe.prev
        else:
            while self._probe is not None and target >= self._probe.data:
                if target == self._probe.data:
                    return True
                else:
                    self._probe = self._probe.next
        return False
        

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
    print("search")
    print(L.probing(37))
    print(L.probing(13))
    print(L.probing(74))
    L.insert(50)
    L.insert(5)
    L.insert(80)
    L.remove(50)
    L.remove(5)
    L.remove(80)
    L.remove(21)
    L.remove(37)
    print("traver")
    L.traversal()
    
