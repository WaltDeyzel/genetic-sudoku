from numpy import random as npR
import numpy as np

def crossover(option_1, option_2, option_3):
    # This function joins two strands of DNA to make a new one.

    dna_1 = option_1.getDNA()
    dna_2 = option_2.getDNA()
    dna_3 = option_3.getDNA()
   
    if npR.uniform() < 0.5:
        return col(dna_1, dna_2, dna_3)
    return row(dna_1, dna_2, dna_3)

def row(dna_1, dna_2, dna_3):

    child = np.zeros((9,9))
    
    # Copy rows [0,3], [3,6], [6,9] from different DNA to child
    child[0:3, :] = dna_1[0:3, :]
    child[3:6, :] = dna_2[3:6, :]
    child[6:9, :] = dna_3[6:9, :]
    
    return(child)

def col(dna_1, dna_2, dna_3):

    child = np.zeros((9,9))

    # Copy columns [0,3], [3,6], [6,9] from different DNA to child
    child[:, 0:3] = dna_1[:, 0:3]
    child[:, 3:6] = dna_2[:, 3:6]
    child[:, 6:9] = dna_3[:, 6:9]

    return child
