#divide and conquer strategy
#

# running time O(log(n))
def binarySearch(theValues, target):
    # Start with the entire squence of elements
    low = 0
    high = len(theValues) - 1
    
    # Repeatedly subdivide the sequence in half unitl the target is found
    while low <= high:
        # find the midpoint of the sequence
        mid = (high + low) // 2
        print(theValues[mid])
        # Does the midpoint contain the target?
        if theValues[mid] == target:
            return True
        # or does the target precede the midpoint
        elif theValues[mid] > target:
            high = mid - 1
        # or does if follow the midpoint
        else:
            low = mid + 1

    # if the sequence cannot be subdivided futher, done
    return False
        
