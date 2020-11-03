# Hamming distance fitness function 
# to find how much the candidate matches the input 
def get_fitness(input_string, candidate_string):
    fitness = 0
    for n in range(len(input_string)):
        if input_string[n] != candidate_string[n]:
            fitness += 1
    return fitness



