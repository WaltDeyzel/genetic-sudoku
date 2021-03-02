import numpy as np
from numpy import random as npR 
from random import randint
from generate import populateSquare

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
        for num in self.col_sum:
            score += abs(num-45)**3
        
        for num in self.row_sum:
            score += abs(num-45)**3

        # UNIQUE 
        for row in self.dna:
            score += (9-np.unique(row).size)**2*100

        for i in range(9):
            score += (9-np.unique(self.dna[:,i]).size)*100
        
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
    
    def mutateSquare(self, problem_grid):
        
        col = 3*randint(0,2)
        row = 3*randint(0,2)
            
        problem_square = problem_grid[row:row+3, col:col+3]

        square = populateSquare(problem_square)

        self.dna[row:row+3, col:col+3] = square
    

    def mutate(self, problem_grid):

        if npR.uniform() < 0.5:
            self.mutateSell(problem_grid)
        self.mutateSquare(problem_grid)



if __name__ == "__main__":

    Ted = Genome(10)