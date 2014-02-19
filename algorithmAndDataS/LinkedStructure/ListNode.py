#linked structure

class ListNode:
    
    def __init__( self, data ):
        self.data = data
        self.next = None

    

def traversal( head ):
    curNode = head
    while curNode is not None:
        print curNode.data
        curNode = curNode.next

def unorderedSearch( head, target ):
    curNode = head
    Ndx = 0
    while curNode is not None and curNode.data != target:
        curNode = curNode.next
        Ndx += 1
   
    return curNode is not None

# Given the head pointer, insert a value into a sorted linked list
# Find the insertion point for the new value
def inserting( head, target ):
    predNode = None
    curNode = head
    while curNode is not None and curNode.data < target:
        predNode = curNode
        curNode = curNode.next
    # Create the new node for the value
    newNode = ListNode( target )
    newNode.next = curNode
    # Link the new node into the list
    if curNode is head:
        head = newNode
    else:
        predNode.next = newNode
    return head

# Head external reference
def prepend( head, item ):
    newNode = ListNode(item)
    newNode.next = head
    head = newNode
    return head

# Tail external reference
def append( tail, item ):
    newNode = ListNode( item )
    if tail is None:
        tail = newNode

    else:
        tail.next = newNode
    tail = newNode
    return tail


def remove( head, target ):
    curNode = head
    preNode = None
    while curNode is not None and curNode.data != target:
        preNode = curNode
        curNode = curNode.next
        
    if curNode is not None:
        if curNode is head:
            head = head.next
        else:
            preNode.next = curNode.next
    return head


def sortedSearch( head, target ):
    curNode = head
    while curNode is not None and curNode.data < target:
        if curNode.data == target:
            return True
        else:
            curNode = curNode.next
    return False
