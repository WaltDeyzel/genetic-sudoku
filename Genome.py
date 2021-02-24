import numpy as np
from numpy import random as npR 
import math
from random import randint
import time

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
        #ans = np.zeros((3,3))

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

        # start_x = 0
        # start_y = 0
        # for r in range(3):
        #     for c in range(3):
        #         square = self.dna[start_y:start_y+3,start_x:start_x+3]
        #         total = np.sum(np.sum(square))
        #         ans[r][c] = total
        #         score += abs(total-45)

        #         start_x += 3
        #         if start_x >= 9:
        #             start_x = 0
        #     start_y += 3
        # self.square_sum = ans
        
        self.fit = 1/(score)
    
    def mutateSell(self, problem_grid):

        #if npR.uniform() < 0.5:
            
        #Random row
        # print(self.dna)
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
        # print(self.dna)
        # time.sleep(100)




if __name__ == "__main__":

    Ted = Genome(10)