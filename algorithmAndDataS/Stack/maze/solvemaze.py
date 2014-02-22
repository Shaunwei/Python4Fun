# program for buidling and solve a maze
from maze import Maze

# the main routine
def main():
    maze = buildMaze( "mazefile.txt" )
    if maze.findPath() :
        print( "Path found...")
        maze.draw()
    else :
        print( "Path not found...")
        

# Builds a maze based on a text format in the given file
def buildMaze( filename ):
    infile = open( filename, "r" )
    
    # Read the size of the maze
    nrows, ncols = readValuePair( infile )
    maze = Maze( nrows, ncols )
    
    # Read the strating and exit position
    row, col = readValuePair( infile )
    maze.setStart( row, col )
    row, col = readValuePair( infile )
    maze.setExist( row, col )
    
    # Read the maze itself
    for row in range( nrows ):
        line = infile.readline()
        for col in range( len(line)):
            if line[col] == "*":
                maze.setWall( row, col )
                
    # Close the maze file and return the newly constructed maze
    infile.close()
    return maze

# Extracts an integer value pair from the given input file
def readValuePair( infile ):
    line = infile.readline()
    valA, valB = line.split()
    return int(valA), int(valB)


# Call the main rout
if __name__=="__main__":
    main()
