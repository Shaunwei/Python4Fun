class ListNode:
    def __init__( self, data ):
        self.data = data
        self.next = None
a = ListNode( 11)
b = ListNode( 52)
c = ListNode( 96 )
a.next = b
b.next = c
print( a.data)
print(a.next.data)
print(a.next.next.data)
