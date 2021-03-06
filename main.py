import numpy as np 
from numpy import random as npR
from generate import generate
from Genome import Genome
from Selection import tournamentSelection
from Crossover import crossover
from inputSudoku import image_input, input_puzzle
from outputSudoku import image_output
import time
import operator
from cv2 import cv2
t = round(time.time())
print(t)
np.random.seed(t)

def show(i):
    print()
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
    print('---------------------------------------------')

if __name__ == "__main__":
    # Manual grid imput method
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
    # Name of puzzle image 
    img = 'puzzle.png'  
    # Locate Sudoku grid and return only the grid
    puzzle_img = image_input(img)
    cv2.imshow('shapes', puzzle_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Use puzzle image to automatically fill in the problem_grid and also return copies of the digit images.
    problem_grid, digits = input_puzzle(puzzle_img)
    
    print(problem_grid)

    # Input parameters
    population_total = 250
    mutation_rate = 0.45
    crossover_rate = 1
    simulations = 100 * 1000

    population = []
    best_genome = None

    # Fill population list
    for _ in range(population_total):
        genome_dna = generate(problem_grid)
        population.append(Genome(genome_dna))
    # Run generations starting at Gen: 0   
    for i in range(simulations):
        population_fitness = 0
        
        for genome in population:
            genome.fitness()
            population_fitness += genome.getFitness()

        sorted_population = population.copy()
        best_genome = max(population, key=operator.attrgetter('fit'))

        if i%1000 == 0:
            show(i)
            image_output(puzzle_img, best_genome.getDNA(), digits)
            
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
                new_genome.mutate(problem_grid)

            population.append(new_genome)
        
    show(i)
    image_output(puzzle_img, best_genome.getDNA(), digits)
     