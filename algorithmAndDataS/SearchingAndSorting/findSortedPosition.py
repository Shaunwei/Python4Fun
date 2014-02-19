# modified version of binary search that returns the index
# within a sorted sequence indication where the target
# shold be located

def findSortedPosition( theList, target):
    low = 0
    high = len(theList) - 1
    while low <= high:
        mid = (low+high)//2
        if theList[mid] == target:
            return mid       # index of the target
        elif theList[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
        
    return low  # index where the target value should be
