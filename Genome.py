import numpy as np
from numpy import random as npR 
from random import randint
from generate import populateSquare
from generate import checkForErrorInGrid

class Genome:

    def __init__(self, dna):
        self.dna = dna
        self.fit = 1
        self.col_sum = None
        self.row_sum = None
        self.square_sum = None
    
    def getDNA(self):
        return(self.dna)

    def getFitness(self):
        return(self.fit)
    
    def fitness(self):

        self.col_sum = np.sum(self.dna, axis=0)
        self.row_sum = np.sum(self.dna, axis=1)

        score = 0

        # UNIQUE 
        for row in self.dna:
            score += (9-np.unique(row).size)**2

        for i in range(9):
            score += (9-np.unique(self.dna[:,i]).size)**2
        
        self.fit = 1/(score)
    
    def mutateSell(self, problem_grid):

        col = 3*randint(0,2)
        row = 3*randint(0,2)
            
        problem_square = problem_grid[row:row+3, col:col+3]

        problem_num_1 = 1
        problem_num_2 = 1

        while problem_num_1 != 0 or problem_num_2 != 0:
            r_1, c_1 = randint(0,2),randint(0,2)
            problem_num_1 = problem_square[ r_1, c_1]
            r_2, c_2 = randint(0,2),randint(0,2)
            problem_num_2 = problem_square[ r_2, c_2]

        copy = self.dna[row+r_1, col+c_1].copy()
        self.dna[row+r_1, col+c_1] = self.dna[row+r_2, col+c_2]
        self.dna[row+r_2, col+c_2] = copy
            
    def mutateSellSmart(self):
        # This function swops two numbers that are wrong but only if the swop will 
        # result in a solution with fewer erros.

        # Create copy of current grid
        grid = self.dna.copy()
        # Get all the erros
        errCorrs = checkForErrorInGrid(grid)
        # Current number of errors of the grid
        numberErrorsGrid = errCorrs.shape[0]
        # Flag for when a swop occurs
        swop = False
        # The coordinates of errCorrs is stored [x, y] but when we loop we loop row and collumns
        # Rows are y and collumns are x. So it needs to be inverted. 
        # TODO: change implementation in checkForErrorInGrid
        x = 0
        y = 1
        
        # Get two coordinates of errCorrs
        for cor in errCorrs:
            for otherCor in errCorrs:
                # If the coordinates are the same get a new number. Must be different
                if not np.array_equal(cor, otherCor):
                    # Loop through 3x3 square. Both coordinates must be in square
                    for br in range(3):
                        for bc in range(3):
                            # Loop through 9 squares
                            # If both cors are within that square proceed
                            Y1B = cor[1] >=  br*3 
                            Y1T = cor[1] <  br*3+3
                            Y2T = otherCor[1] <  br*3+3
                            Y2B = otherCor[1] >  br*3
                            if Y1B and Y1T and Y2B and Y2T:
                                X1B = cor[0] > bc*3
                                X1T = cor[0] <  bc*3+3
                                X2T = otherCor[0] <  bc*3+3
                                X2B = otherCor[0] >  bc*3 
                                if X1B and X1T and X2B and X2T:
                                    # Swop the two values 
                                    temp = grid[cor[y], cor[x]]
                                    grid[cor[y], cor[x]] = grid[otherCor[y], otherCor[x]]
                                    grid[otherCor[y], otherCor[x]] = temp
                                    
                                    # Check if it improved layout by reducing the number of erros
                                    errCorrs2 = checkForErrorInGrid(grid)
                                    numberErrorsGrid2 = errCorrs2.shape[0]
                                    
                                    if numberErrorsGrid2 < numberErrorsGrid:
                                        # If it improved the layout by reducing the number of errors
                                        # Swop DNA
                                        # print("SWOP", br, bc)
                                        temp = self.dna[cor[y], cor[x]]
                                        self.dna[cor[y], cor[x]] = self.dna[otherCor[y], otherCor[x]]
                                        self.dna[otherCor[y], otherCor[x]] = temp
                                        swop = True
                                    else:
                                        # Otehrwise
                                        # Swop back
                                        temp = grid[otherCor[y], otherCor[x]]
                                        grid[otherCor[y], otherCor[x]] = grid[cor[y], cor[x]]
                                        grid[cor[y], cor[x]] = temp
                            if swop:
                                break
                        if swop:
                            break  
                if swop:
                    break 
            if swop:
                break

    def mutateSquare(self, problem_grid):
        
        col = 3*randint(0,2)
        row = 3*randint(0,2)
            
        problem_square = problem_grid[row:row+3, col:col+3]

        square = populateSquare(problem_square)

        self.dna[row:row+3, col:col+3] = square
    

    def mutate(self, problem_grid):
        # This function mutates the DNA bases on a mutation function. 
        # Input : 
        #       problem_grid : Original grid with starting layout to 
        #                      use as reference to not mutate the wrong 
        #                       cells 
        
        if npR.uniform() < 0.8:
            # Smart mutation 
            self.mutateSellSmart()
        else:
            # Random mutation 
            self.mutateSquare(problem_grid)
        

if __name__ == "__main__":
    problem_grid = np.array([
    [0,0,7, 7,8,0, 0,0,0],
    [0,0,5, 5,9,0, 0,0,0],
    [0,0,0, 0,0,0, 0,0,0],

    [0,0,0, 0,0,2, 2,0,0],
    [0,0,0, 0,0,7, 7,0,0],
    [0,0,0, 0,0,0, 0,0,0],

    [0,0,0, 0,0,4, 4,0,0],
    [0,0,0, 0,0,3, 3,0,0],
    [0,0,0, 0,0,0, 0,0,0],
    ])
    Ted = Genome(problem_grid)
    
    Ted.mutate(problem_grid)
    Ted.mutate(problem_grid)
    Ted.mutate(problem_grid)
    print(Ted.dna)