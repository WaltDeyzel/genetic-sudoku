import time
def crossover(option_1, option_2, option_3):

    dna_1 = option_1.getDNA()
    dna_2 = option_2.getDNA()
    dna_3 = option_3.getDNA()
   
    child_1 = dna_1.copy()
    
    child_1[0:3, :] = dna_1[0:3, :]
    child_1[3:6, :] = dna_2[3:6, :]
    child_1[6:9, :] = dna_3[6:9, :]
    
    return(child_1)