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

def checkForErrorInGrid(problem_grid):
    # This function returns the coordinates of numbers that appear in the same row and/or column
    # Coordinates of the numbers that are in the same row or column
    coordinates = []
    # Index of error for coordinates
    idxError = 0;

    for r in range(9):
        for c in range(9):
            # Current number at coordinate [r,c]
            value_1 = problem_grid[r,c]
            if value_1 == 0:
                continue
            # Check row
            for idx in range(9):
                # Do not compare to itself
                if c != idx:
                    # Number at coordinate [r, idx]
                    value_2 = problem_grid[r, idx]
                    # Skip zeros
                    if value_2 == 0:
                        continue
                    # If the numbers are the same an error
                    if value_1 == value_2:  
                        # Store [c, r]  {NOT! [r, c] because c -> x and r -> y} in coordinates
                        coordinates.append([c, r])
                        continue
                    
            # Check column
            for idy in range(9):
                # Do not compare to itself
                if r != idy:
                    value_2 = problem_grid[idy, c]
                    # Skip zeros
                    if value_2 == 0:
                        continue
                    # If the numbers are the same an error
                    if value_1 == value_2:  
                        # Store [c, r]  {NOT! [r, c] because c -> x and r -> y} in coordinates
                        coordinates.append([c, r])
                        continue
    # Doubles can occur when number is in the same row and in the same column
    # find unique coordinates [r, c]
    uniqueCoordinates = np.unique(coordinates, axis=0)
    return uniqueCoordinates
            
if __name__ == '__main__':
    problem_grid = np.array([
    [0,0,0, 0,0,0, 0,0,0],
    [0,2,0, 0,0,0, 0,0,0],
    [0,0,0, 0,3,0, 0,3,0],

    [0,0,0, 0,0,0, 0,0,0],
    [0,2,0, 0,0,0, 0,0,0],
    [0,0,0, 0,4,4, 4,0,0],

    [1,0,0, 0,0,0, 0,0,0],
    [0,2,0, 0,0,0, 0,0,0],
    [1,0,0, 0,0,0, 0,0,0],
    ])
     
    print(checkForErrorInGrid(problem_grid))