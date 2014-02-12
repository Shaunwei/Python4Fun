# Implementation of the Set ADT container using a Python List
class Set:
    # Creates an empty set instance
    def __init__( self ):
        self._theElements = list()
        
    # Returns the number of items in the set
    def __len__( self ):
        return len( self._theElements )

    # Documents if an element is in the set
    def __contains__( self, element ):
        return element in self._theElements

    # Adds a new unique element to the set
    def add( self, element ):
        if element not in self:
            self._theElements.append( element )
            
    # Remove an element from the set
    def remove( self, element ):
        assert element in self, "The element must be in the set"
        self._theElements.remove( element )

    # Determines if two sets are equal
    def __eq__( self, setB ):
        if len( self )!= len( setB ):
            return False
        else :
            return self.isSubsetOf( setB )

    # Determines if this set is a subset of setB
    def isSubsetOf( self, setB):
        for element in self:
            if element not in setB:
                return False
        return True
    
    # Creates a new set from the union of this set and SetB
    def union( self, setB):
        newSet = Set()
        newSet._theElements.extend( self._theElements )
        for element in setB:
            if element not in self:
                newSet._theElements.append( element )
        return newSet

    # Create a newset from the intersection: self set and setB
    def interset( self, setB ):
        newSet = Set()
        for element in self:
            if element in setB:
                newSet._theElements.append( element )
        return newSet

    # Create a new  set from the diff: self and setB
    def difference(self, setB):
        newSet = Set()
        for element in self:
            if element not in setB:
                newSet._theElements.append( element )
        return newSet

    # Return an itertor for traversing the list of items
    def __iter__(self):
        return _SetIterator( self._theElements )
        

class _SetIterator:
    
    def __init__(self, theSet):
        pass
