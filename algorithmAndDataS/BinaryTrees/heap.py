# implemetation of heap( a complete binary tree)

class MaxHeap:
    def __init__(self):
        self._elements = []
        self._count = 0
        
    def __len__(self):
        return self._count
    
    def add(self, value):
        self._elements[self._count] = value
        self._count += 1
        self._siftUp(self._count-1)
        
    def extract(self):
        assert self._count > 0, "Cannot extract from an empty heap."
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        self._siftDown(0)
        
    def _siftUp(self, ndx):
        if ndx > 0:
            parent = ndx // 2
            if self._elements[ndx] > self._elements[parent]:
                self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx] 
                self._siftUp(parent)
                
    def _siftDown(self, ndx):
        left = 2*ndx + 1
        right = 2*ndx + 2
        current = ndx
        largest = __find_largest(left, right, current)
        if largest != current:
            self._elements[current], self.elements[largest] = self._elements[largest], self.elements[current]
        
    def __find_largest(self, left, right, current):
        largest = current
        if self._elements[left] >= self._elements[largest]:
            largest = left
        elif self._elements[right] >= self._elements[largest]:
            largest = right
        else:
            largest = current
        return largest
        
