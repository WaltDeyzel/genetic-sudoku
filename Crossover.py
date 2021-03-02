from numpy import random as npR

def crossover(option_1, option_2, option_3):

    dna_1 = option_1.getDNA()
    dna_2 = option_2.getDNA()
    dna_3 = option_3.getDNA()
   
    if npR.uniform() < 0.5:
        return col(dna_1, dna_2, dna_3)
    return row(dna_1, dna_2, dna_3)

def row(dna_1, dna_2, dna_3):

    child = dna_1.copy()
    
    child[0:3, :] = dna_1[0:3, :]
    child[3:6, :] = dna_2[3:6, :]
    child[6:9, :] = dna_3[6:9, :]
    
    return(child)

def col(dna_1, dna_2, dna_3):

    child = dna_3.copy()
    
    child[:, 0:3] = dna_1[:, 0:3]
    child[:, 3:6] = dna_2[:, 3:6]
    child[:, 6:9] = dna_3[:, 6:9]

    return child
