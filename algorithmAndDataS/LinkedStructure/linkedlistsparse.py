# Implementation of the Sparse Matrix ADT using an array of linked lists
#from array import Array

class SparseMatrix:
    # Creates a sparse matrix of size numRows x numCols initialized to 0
    def __init__( self, numRows, numCols ):
        self._numCols = numCols
        self._listOfRows = Array( numRows )
        
    # Returns the number of rows in the matrix
    def numRows( self ):
        return len( self._listOfRows )
    
    # Returns the number of columns in the matrix
    def numCols( self ):
        return self._numCols
    
    # Returns the value of element(i,j) : x[i,j]
    def __getitem__( self, ndxTuple ):
        pass
    
    # Sets the value of element (i,j) to the value : x[i,j] = s
    def __setitem__( self, ndxTuple, value ):
        predNode = None
        curNode = self._listOfRows[row]
        while curNode is not None and curNode.col != col:
            predNode = curNode
            curNode = curNode.next
            
        # See if the element is in the list
        if curNode is not None and curNode.col == col:
            if value == 0.0 :   # remove the node
                if curNode == self._listOfRows[row]:
                    self._listOfRows[row] = curNode.next
                else:
                    predNode.next = curNode.next
            else:     #change the node's value
                curNode.value = value

        # Otherwise, the element is not in the list
        elif value != 0.0 :
            newNode = _MatrixElementNode( col, value )
            newNode.next == curNode
            if curNode == self._listOfRows[row]:
                self._lisfOfRows[row] = newNode
            else:
                predNode.next = newNode
                
        # Scales the matrix by the given scalar
        def scaleBy( self, scalar ):
            for row in range( self.numRows() ):
                curNode = self._listOfRows[row]
                while curNode is not None:
                    curNode.value *= scalar
                    curNode = curNode.next
                
        # Creates and returns a new matrix that is the transpose of this matrix
        def transpose( self, scalar ):
            pass
        
        # Matrix addition: newMatrix = self + rhsMatrix
        def __add__( self, rhsMatrix ):
            # Make sure the two matrices have the corrent size
            assert rhsMatrix.numRows() == self.numRows() and \
                   rhsMatrix.numCols() == self.numCols(), \
                   "Matrix sizes not compatable for adding."
            
            # Create a new sparse matrix of the same size
            newMatrix = SparseMatrix( self.numRows(), self.numCols())
            
            # Add the elements of this matrix to the new matrix
            for row in range( self.numRows()):
                curNode = self._listOfRows[row]
                while curNode is not None:
                    newMatrix[row, curNode.col] = curNode.value
                    curNode = curNode.next
                    
            # Add the elements of the rhsMatrix to the new matrix
            for row in range( rhsMatrix.numRows()):
                curNode = rhsMatrix._listOfRows[row]
                while curNode is not None:
                    value = newMatrix[row, curNode.col]
                    value += curNode.value
                    newMatrix[row, curNode.col] = value
                    curNode = curNode.next
                    
            # Return the new matrix
            return newMatrix
        
        #--- Matrix substraction and multiplication ---
        # def __sub__( self, rhsMatrix ):
        # def __mul__( self, rhsMatrix ):
        

# Storage class for creating matrix element nodes
class _MatrixElementNode:
    def __init__( self, col, value ):
        self.col = col
        self.value = value
        self.next = Node

        
