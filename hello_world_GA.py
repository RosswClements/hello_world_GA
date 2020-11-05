import random
import string

population_size = 10
population = []
new_population = []

def main():
    input_string = input("Please enter a string: ")
    best_fit = len(input_string)

    init_pop(population_size, input_string, population)
    print(population)

    while best_fit > 0:
    eval_pop(population, input_string)
    crossover(new_population)

# generate random string with digits, letters, spaces, and special characters
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
    print(f"Fitness is: {fitness}")
    return fitness

#evaluate population and begin a new population from the fittest
def eval_pop(population, input_string):
    second_fit = len(input_string)
    third_fit = len(input_string)
    fourth_fit = len(input_string)
    for pop in population:
        get_fitness(input_string, pop)
        # if fitness is 0 solution is found
        if fitness == 0:
            best_fit = 0
            return best_fit
        elif fitness <= best_fit:
            #add to index 0 as elitism
            new_population[0] = pop
            #and the top 4 fittest to corresponding indexes for crossover
            new_population[1] = pop
            best_fit = fitness
        elif fitness > best_fit and <= second_fit:
            new_population[2] = pop
            second_fit = fitness
        elif fitness > second_fit and <= third_fit:
            new_population[3] = pop
            third_fit = fitness
        elif fitness > third_fit and <= fourth_fit:
            new_population[4] = pop
            fourth_fit = fitness
        else:
            pass
    return new_population

def crossover(new_population):

def mutate(new_population):





            
main()