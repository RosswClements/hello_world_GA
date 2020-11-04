import random
import string

def main():
    population_size = 8
    population = []
    input_string = input("Please enter a string: ")

    init_pop(population_size, input_string, population)
    print(population)

# generate random string with digits letters and special characters
def generate_candidate_string(input_string):
    candidate_string = string.ascii_letters + string.digits + string.punctuation+ ' '
    candidate = ''.join(random.choice(candidate_string) for _ in range(len(input_string)))
    return candidate

# initial population
def init_pop(population_size, input_string, population):
    for _ in range(population_size):
        candidate = generate_candidate_string(input_string)
        population.append(candidate)
    return(population)

# Hamming distance fitness function 
# to find how much the candidate matches the input 
def get_fitness(input_string, candidate_string):
    fitness = 0
    for n in range(len(input_string)):
        if input_string[n] != candidate_string[n]:
            fitness += 1
    return fitness



main()