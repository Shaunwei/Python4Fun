# Implemetation of the Queue ADT using a Python list
class Queue:
    # Create an empty list
    def __init__( self ):
        self._qList = list()
        
    # Return True if the queue is empty
    def isEmpty( self ):
        return len( self ) == 0

    # Return the number of items in the queue
    def __len__( self ):
        return len(self._qList)
    
    # Adds the given item to the queue
    def enqueue( self, item ):
        self._qList.append( item )
        
    # Remove and returns the first item in the queue
    def dequeue( self ):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        return self._qList.pop( 0 )
    
    
