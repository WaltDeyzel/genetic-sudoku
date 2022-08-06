import numpy as np

def generate(problem_grid):
    # This function generates a filled puzzle grid.
    
    # Example problem grid
    # [4,0,0, 6,0,0, 3,0,0],
    # [0,0,2, 8,0,0, 4,0,0],
    # [3,0,0, 5,9,0, 0,0,0],

    # [0,7,0, 0,0,0, 0,0,2],
    # [0,2,0, 0,3,0, 0,1,5],
    # [1,0,0, 9,0,0, 0,0,4],

    # [0,0,0, 1,7,0, 9,0,0],
    # [0,0,0, 0,0,0, 0,2,8],
    # [0,9,0, 0,0,0, 0,0,3],
    
    grid = problem_grid.copy()
    
    # Loop over 3x3 square in puzzle 
    for r in range(3):
        for c in range(3):
            
            square = grid[r*3:r*3+3,c*3:c*3+3]
            grid[r*3:r*3+3,c*3:c*3+3] = populateSquare(square) 
        
    return(grid)


def populateSquare(grid):
    # This function populates a 3x3 square with numbers 1-9.
    # If a number already appears by default skip that number and continue.
    
    # e.g grid:
    # [ 0 2 0 ]
    # [ 4 0 0 ]
    # [ 0 0 9 ]
    # default numbers are 2, 4, 9
    
    # Create copy of grid
    square = grid.copy()
    # Available Numbers to fill a 3x3 grid.
    options = [1,2,3,4,5,6,7,8,9]

    for row in square:
        for num in row:
            
            if num in options:
                # Remove e.g 2,4 and 9 from options because it already appears in grid
                options.remove(num)
            
    for r in range(3):
        for c in range(3):
            if square[r,c] == 0:
                # Options should only contain the numbers (1, 3, 5, 6, 7, 8 ) that do not appear in grid;
                val = np.random.choice(options, 1)
                # Fill random number in an empty spot ( 0 )
                square[r,c] = val
                # Remove val from options
                options.remove(val)
    return square
