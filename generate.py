import numpy as np

def generate(problem_grid):

    grid = problem_grid.copy()
    #grid = np.zeros((9,9))
    


    start_x = 0
    start_y = 0
    for r in range(3):
        for c in range(3):
            options = [1,2,3,4,5,6,7,8,9]
            square = grid[start_y:start_y+3,start_x:start_x+3]

            for row in square:
                for num in row:

                    if num in options:
                        options.remove(num)
                        #print(options)
            
            for r in range(3):
                for c in range(3):
                    if square[r,c] == 0:
                        val = np.random.choice(options, 1)
                        square[r,c] = val
                        options.remove(val)

            grid[start_y:start_y+3,start_x:start_x+3] = square
                
            start_x += 3
            if start_x >= 9:
                start_x = 0
        start_y += 3    
        
    return(grid)


if __name__ == "__main__":

    pass