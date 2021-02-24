import numpy as np 
from generate import generate
from Genome import Genome
import operator
from Selection import tournamentSelection
from numpy import random as npR
from Crossover import crossover
import time

t = round(time.time())
print(t)
np.random.seed(t)

def show(i):
    print('---------------------------------------------')
    print('Gen:', i, '--> ', round(1/best_genome.getFitness()))
    dna = best_genome.getDNA()
    n = 1
    for row in dna:
        print(row[0:3], row[3:6], row[6:9])
        if n % 3 == 0:
            print()
        n+=1
    print()
    print(best_genome.col_sum)
    print(best_genome.row_sum)
    print()
    print(best_genome.square_sum)
    print()
    print('---------------------------------------------')

if __name__ == "__main__":
    problem_grid = np.array([
        [0,0,0, 2,6,0, 7,0,1],
        [6,8,0, 0,7,0, 0,9,0],
        [1,9,0, 0,0,4, 5,0,0],

        [8,2,0, 1,0,0, 0,4,0],
        [0,0,4, 6,0,2, 9,0,0],
        [0,5,0, 0,0,3, 0,2,8],

        [0,0,9, 3,0,0, 0,7,4],
        [0,4,0, 0,5,0, 0,3,6],
        [7,0,3, 0,1,8, 0,0,0],
        ])

    
    print(problem_grid)
    population_total = 150
    mutation_rate = 0.3
    crossover_rate = 1

    population = []
    best_genome = None

    for _ in range(population_total):
        genome_dna = generate(problem_grid)
        population.append(Genome(genome_dna))
        
    for i in range(100000):
        population_fitness = 0
        
        for genome in population:
            genome.fitness()
            population_fitness += genome.getFitness()

        sorted_population = population.copy()
        best_genome = max(population, key=operator.attrgetter('fit'))

        if i%5000 == 0:
            show(i)
            
        if round(1/best_genome.getFitness()) <= 1:
            print('Done')
            break
        population.clear()
        population.append(best_genome)
        

        while len(population) < population_total:

            new_genome = tournamentSelection(sorted_population)
            option_2 = tournamentSelection(sorted_population)

            if npR.uniform() < crossover_rate:
                option_3 = tournamentSelection(sorted_population)
                dna_1 = crossover(new_genome, option_2, option_3)
                new_genome = Genome(dna_1)

            if npR.uniform() < mutation_rate:
                new_genome.mutateSell(problem_grid)

            population.append(new_genome)
        
    show(i)
     