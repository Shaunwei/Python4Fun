# Implement the maze ADT using 2-d array
from array import Array2D
from linkliststack import Stack

class Maze:
    # Define constants to represent contents of the maze cell
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"
    
    def __init__( self, num_rows, num_cols ):
        self._maze_cells = Array2D( num_rows, num_cols )
        self._start_cell = None
        self._exit_cell = None
        
    def num_rows( self ):
        return self._maze_cells.num_rows()
    
    #not finished
    #page 216
