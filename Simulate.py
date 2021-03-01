import numpy as np 
from numpy import random as npR
from generate import generate
from Genome import Genome
from Selection import tournamentSelection
from Crossover import crossover
import operator
import time
import matplotlib.pyplot as plt


class Simulate:

    def __init__(self, problem_grid, population_total, mutation_rate, crossover_rate, simulations, limit):
        self.problem_grid = problem_grid
        self.population_total = population_total
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.simulations = simulations
        self.limit = limit 
    
    def show(self, i, best_genome):
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
        print(best_genome.row_sum)
        print(best_genome.col_sum)
        print()
        print(best_genome.square_sum)
        print()
        

    def run(self):

        population = []
        best_genome = None
        data = []

        for _ in range(population_total):
            genome_dna = generate(problem_grid)
            population.append(Genome(genome_dna))
            
        for i in range(simulations):
            population_fitness = 0
            
            for genome in population:
                genome.fitness()
                population_fitness += genome.getFitness()

            sorted_population = population.copy()
            best_genome = max(population, key=operator.attrgetter('fit'))
            best_fitness = round(1/best_genome.getFitness())
            data.append(best_fitness)

            if i%1000 == 0:
                self.show(i, best_genome)
                    
            if  best_fitness <= limit:
                print('DONE\n')
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

                
        self.show(i, best_genome)
        return data


if __name__ == "__main__":
    problem_grid = np.array([
        [4,0,0, 6,0,0, 3,0,0],
        [0,0,2, 8,0,0, 4,0,0],
        [3,0,0, 5,9,0, 0,0,0],

        [0,7,0, 0,0,0, 0,0,2],
        [0,2,0, 0,3,0, 0,1,5],
        [1,0,0, 9,0,0, 0,0,4],

        [0,0,0, 1,7,0, 9,0,0],
        [0,0,0, 0,0,0, 0,2,8],
        [0,9,0, 0,0,0, 0,0,3],
        ])
    
    population_total = 100
    mutation_rate = 0.35
    crossover_rate = 1
    simulations = 500
    limit = 1
    
    for _ in range(1):
        for i in range(5):
            Jeff = Simulate(problem_grid, population_total, i/100, crossover_rate, simulations, limit)
            name = "mutate-" + str(i) +".png"
            plt.plot(Jeff.run())
        plt.savefig(name, bbox_inches='tight')
        plt.close()
    #plt.show()
    
