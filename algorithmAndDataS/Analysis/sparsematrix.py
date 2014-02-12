# Implementation of the sparse matrix ADT using list

class SparseMatrix :
    # Create a sparse matrix of size numRows x numCols initialized to 0
    def __init__( self, numRows, numCols ):
        self._numRows = numRows
        self._numCols = numCols
        self._elementList = list()
        
    # Return the number of rows in the matrix
    def numRows( self ):
        return self._numRows
    
    # Return the number of columns in the matrix
    def numCols( self ):
        return self._numCols
    
    # Return the value of element(i,j): x[i,j]
    def __getitem__(self, ndxTuple):
        pass

    # Set the value
