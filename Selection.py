from numpy import random as npR

def tournamentSelection(sorted_population):
    gap = sorted_population.shape[0]
    x_1 = int(npR.uniform()*gap)
    x_2 = int(npR.uniform()*gap)

    option_1 = sorted_population[x_1]
    option_2 = sorted_population[x_2]

    if option_1.getFitness() < option_2.getFitness():
        return option_2
    return option_1


