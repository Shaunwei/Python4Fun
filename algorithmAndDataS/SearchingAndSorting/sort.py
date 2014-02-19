#

#Selection Sort
# O(n^2)
def selectionSort( theSeq ):
    n = len(theSeq)
    for i in range(n-1):
        smallNdx = i
        for j in range(i+1, n):
            if theSeq[j] < theSeq[smallNdx] :
                smallNdx = j

    if smallNdx != i:
        theSeq[smallNdx], theSeq[i] = theSeq[i], theSeq[smallNdx]



#insertionSort
def insertionSort(theSeq):
    n = len(theSeq)
    # starts with the first item as the only sorted entry
    for i in range(1,n):
        # save the value to be positioned
        value = theSeq[i]
        print(value, i )
        pos = i
        while pos > 0 and value < theSeq[pos-1]:
            theSeq[pos] = theSeq[pos -1]
            pos -= 1

        theSeq[pos] = value
    return theSeq

