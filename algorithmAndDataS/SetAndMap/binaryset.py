#Implementation of the Set ADT using a sorted list

class Set:
    #create an empty set instance
    def __init__(self):
        self._theElements = list()
        
    #returns the number of the items in the set
    def __len__(self):
        return len(self._theElements)
    
    #Determines if an element is in the set
    def __contains__(self, element):
        ndx = self._findPosition( element )
        return ndx < len(self) and self._theElements[ndx] == element
    
    # Determines if two sets are equal
    def __eq__( self, setB ):
        if len( self ) != len( setB ):
            return False
        else:
            for i in range( len(self) ):
                if self._theElements[i] != setB._theElements[i] :
                    return False
            return True
    
    #adds a new unique element to the set
    def add( self, element ):
        if element not in self:
            ndx = self._findPosition( element )
            self._theElements.insert( ndx, element )
            
    #remove an element from the set
    def remove( self, element ):
        assert element in self, "The element must be in the set."
        ndx = self._findPositon( element )
        self._theElements.pop( ndx )
        
    #determines if this set is a subset of setB
    def isSubsetOf( self, setB ):
        for element in self:
            if element not in setB:
                return False
        return True
    
    # The reamining methods go here
    def union( self, setB ):
        newSet = Set()
        a = 0
        b = 0
        # Merge the two lists together until one is empty
        while a < len(self) and b < len(setB):
            vA = self._theElements[a]
            vB = self._theElements[b]
            if vA < vB:
                newSet._theElements.append(vA)
                a += 1
            elif vA > vB:
                newSet._theElements.append(vB)
                b += 1
            else:    # Only one of the two duplicates are appended
                newSet._theElements.append(vA)
                a += 1
                b += 1
        while a < len(self):
            newSet._theElements.append(self._theElements[a])
            a += 1
        while b < len(setB):
            newSet._theElements.append(setB._theElements[b])

        return newSet


    # Returns an iterator for traversing the list of items
    def __iter__( self ):
        return _SetIterator( self._theElements )
    
    # Finds the position of the element within the ordered list
    def _findPosition( self, element ):
        low = 0
        high = len( self ) - 1
        while low <= high :
            mid = (low + high) //2
            if self[mid] == target:
                return mid
            elif target < self[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low
    
    class _SetIterator :
        def __init__( self, listHead ):
            self._curNode = listHead
            
        def __iter__( self ):
            return self
        
        def next( self ):
            if self._curNode is None:
                raise StopIteration
            else :
                item = self._curNode.item
                self._curNode = self._curNode.next
                return item
