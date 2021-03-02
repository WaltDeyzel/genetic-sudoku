import numpy as np

def generate(problem_grid):

    grid = problem_grid.copy()
    
    for r in range(3):
        for c in range(3):
            
            square = grid[r*3:r*3+3,c*3:c*3+3]
            grid[r*3:r*3+3,c*3:c*3+3] = populateSquare(square) 
        
    return(grid)


def populateSquare(grid):
    square = grid.copy()
    options = [1,2,3,4,5,6,7,8,9]

    for row in square:
        for num in row:

            if num in options:
                options.remove(num)
            
    for r in range(3):
        for c in range(3):
            if square[r,c] == 0:
                val = np.random.choice(options, 1)
                square[r,c] = val
                options.remove(val)
    return square

if __name__ == "__main__":

    pass