# Containing different searching method
# linear search

#runing O(n)
def linearSearch( theValues, target ):
    n = len( theValues )
    for i in range( n ):
        if theValues[i] == target:
            return True
    
    return False



#
def sortedLinearSearch( theValues, item):
    n = len(theValues)
    for i in range(n):
        if theValues[i] == item:
            return True
        elif theValues[i] >item:
            return False
        
    return False

#worst case O(n)
def findSmallest( theValues):
    n = len(theValues)
    smallest = theValues[0]
    for i in range(n):
        if theValues[i] < smallest:
            smallest = theValues[i]
    
    return smallest


