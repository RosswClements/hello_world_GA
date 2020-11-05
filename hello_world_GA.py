import random
import string

population_size = 25
population = []
new_population = list(range(population_size))
input_string = input("Please enter a string: ")
fitness = len(input_string)

def main():

    init_pop(population_size, input_string, population)
    print(population)
    print(new_population)

   # while best_fit > 0:
    eval_pop(population, input_string)
    crossover(new_population)
    print(new_population)

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
    #print(f"Fitness is: {fitness}")
    return fitness

#evaluate population and begin a new population from the fittest
def eval_pop(population, input_string):
    best_fit = len(input_string)
    second_fit = len(input_string)
    for pop in population:
        fitness = get_fitness(input_string, pop)
        # if fitness is 0 solution is found
        if fitness == 0:
            return fitness
        elif fitness <= best_fit:
            #add to index 0 as elitism
            new_population.pop(0)
            new_population.insert(0, pop)
            #and the top 2 fittest to corresponding indexes for crossover
            new_population.pop(1)
            new_population.insert(1, pop)
            best_fit = fitness
        elif fitness > best_fit and fitness <= second_fit:
            new_population.pop(2)
            new_population.insert(2, pop)
            second_fit = fitness
        else:
            pass
    print("new population before cross")
    print(new_population)
    for pop in range(len(new_population[4:])):
        new_population.pop()
    for pop in range(population_size-4):
        new_population.append(generate_candidate_string(input_string))
    print("new population after int removal")
    print(new_population)
    return new_population

def crossover(new_population):
    parent1 = new_population[1]

    print(parent1)
    parent2 = new_population[2]

    child1 = []
    child2 = []

    coinflip = 0

    for gene in range(0 , len(parent1)):
        coinflip = random.randint(0,1)
        if coinflip == 0:
            child1.insert(gene, parent1[gene])
            child2.insert(gene, parent2[gene])
        else:
            child1.insert(gene, parent2[gene])
            child2.insert(gene, parent1[gene])

    new_population[1] = ''.join(child1)
    new_population[2] = ''.join(child2)

def mutate(new_population):
    pass
main()