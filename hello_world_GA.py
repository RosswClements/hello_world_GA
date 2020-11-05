import random
import string

population_size = 30
population = []
goal_found = ''
#new_population = list(range(population_size))
new_population = []
input_string = input("Please enter a string: ")
best_fit = len(input_string)
#Hfitness = len(input_string)
mutation_rate = 20


def main():
    global population
    global best_fit
    gen_count = 0

    init_pop(population_size, input_string, population)
    #print(population)
    #init new pop just for ease of working with the list
    init_pop(population_size, input_string, new_population)
    #print(new_population)

    while best_fit != 0:
        eval_pop(population, input_string)
        crossover(new_population)
        #print(new_population)
        mutate(new_population)
        gen_count += 1
        #print(f"{new_population} + {gen_count}")
        population = new_population
        print(f"{population} + {gen_count}")
    print(goal_found)
    print("done")

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
def get_fitness(candidate_string):
    global input_string
    fitness = 0
    for n in range(len(input_string)):
        if input_string[n] != candidate_string[n]:
            fitness += 1
    #print(f"Fitness is: {fitness}")
    return fitness

#evaluate population and begin a new population from the fittest
def eval_pop(population, input_string):
    global best_fit
    global goal_found
    fitness = best_fit
    population.sort(key=get_fitness)
    for pop in population:
        fitness = get_fitness(pop)
        # if fitness is 0 solution is found
        if fitness == 0:
            best_fit = 0
            goal_found = pop
            break
    new_population = population
    print(get_fitness(new_population[0]))
    # second_fit = len(input_string)
    # third_fit = len(input_string)
    # fourth_fit = len(input_string)
    # for pop in population:
    #     fitness = get_fitness(pop)
    #     # if fitness is 0 solution is found
    #     print(get_fitness( population[0]))
    #     if fitness == 0:
    #         best_fit = 0
    #         break
    #     elif fitness <= best_fit and pop != new_population[0]:
    #         #add to index 0 as elitism
    #         # if pop == new_population[0]:
    #         #     break
    #         # else:
    #         new_population.pop(0)
    #         new_population.insert(0, pop)
    #         #and the top 2 fittest to corresponding indexes for crossover
    #         new_population.pop(1)
    #         new_population.insert(1, pop)
    #         best_fit = fitness

    #     elif fitness == best_fit and pop == new_population[0] or fitness == best_fit and pop == new_population[1]:
    #         new_population.pop(2)
    #         new_population.insert(2, generate_candidate_string(input_string))

    #     elif fitness == best_fit and pop != new_population[0] and pop != new_population[1]:
    #         new_population.pop(2)
    #         new_population.insert(2, pop)
    #         new_population.pop(5)
    #         new_population.insert(5, pop)
    #         #second_fit = fitness
        
    #     elif fitness == best_fit and pop != new_population[2]:
    #         # if pop == new_population[3]:
    #         #     break
    #         #else:
    #         new_population.pop(3)
    #         new_population.insert(3, pop)
    # #        second_fit = fitness
    #     elif fitness == best_fit and pop != new_population[3]:
    #         # if pop == new_population[4]:
    #         #     break
    #         #else:
    #         new_population.pop(4)
    #         new_population.insert(4, pop)
    #         second_fit = fitness        
    #     else:
    #         pass
    # #print("new population before cross")
    # #print(new_population)
    # for pop in range(len(new_population[5:])):
    #     new_population.pop()
    # for pop in range(population_size-5):
    #     new_population.append(generate_candidate_string(input_string))
    # #print("new population after int removal")
    # #print(new_population)
    # return new_population

def crossover(new_population):
    parent1 = new_population[1]

    #print(parent1)
    parent2 = new_population[2]
    parent3 = new_population[3]
    parent4 = new_population[4]

    child1 = []
    child2 = []
    child3 = []
    child4 = []
    child5 = []
    child6 = []
    child7 = []
    child8 = []
    child9 = []
    child10 = []
    child11 = []
    child12 = []

    coinflip = 0

    for gene in range(0 , len(parent1)):
        coinflip = random.randint(0,1)
        if coinflip == 0:
            child1.insert(gene, parent1[gene])
            child2.insert(gene, parent2[gene])
        else:
            child1.insert(gene, parent2[gene])
            child2.insert(gene, parent1[gene])

    for gene in range(0 , len(parent3)):
        coinflip = random.randint(0,1)
        if coinflip == 0:
            child3.insert(gene, parent3[gene])
            child4.insert(gene, parent4[gene])
        else:
            child3.insert(gene, parent4[gene])
            child4.insert(gene, parent3[gene])

    for gene in range(0 , len(parent1)):
        coinflip = random.randint(0,1)
        if coinflip == 0:
            child5.insert(gene, parent1[gene])
            child6.insert(gene, parent3[gene])
        else:
            child5.insert(gene, parent3[gene])
            child6.insert(gene, parent1[gene])

    for gene in range(0 , len(parent1)):
        coinflip = random.randint(0,1)
        if coinflip == 0:
            child7.insert(gene, parent2[gene])
            child8.insert(gene, parent3[gene])
        else:
            child7.insert(gene, parent3[gene])
            child8.insert(gene, parent2[gene])

    for gene in range(0 , len(parent1)):
        coinflip = random.randint(0,1)
        if coinflip == 0:
            child9.insert(gene, parent1[gene])
            child10.insert(gene, parent4[gene])
        else:
            child9.insert(gene, parent4[gene])
            child10.insert(gene, parent1[gene])

    for gene in range(0 , len(parent1)):
        coinflip = random.randint(0,1)
        if coinflip == 0:
            child11.insert(gene, parent2[gene])
            child12.insert(gene, parent4[gene])
        else:
            child11.insert(gene, parent4[gene])
            child12.insert(gene, parent2[gene])

    new_population[1] = ''.join(child1)
    new_population[2] = ''.join(child2)
    new_population[3] = ''.join(child3)
    new_population[4] = ''.join(child4)
    new_population[5] = ''.join(child5)
    new_population[6] = ''.join(child6)
    new_population[7] = ''.join(child7)
    new_population[8] = ''.join(child8)
    new_population[9] = ''.join(child9)
    new_population[10] = ''.join(child10)
    new_population[11] = ''.join(child11)
    new_population[12]= ''.join(child12)

    for _ in range(len(new_population[12:])):
        new_population.pop()
    for _ in range(population_size-12):
        new_population.append(generate_candidate_string(input_string))

def mutate(new_population):
    mutation_counter = 0
    while mutation_counter < mutation_rate:
        rand_pop = random.randint(0, len(new_population)-1)
        selected_pop = list(new_population[rand_pop])
        rand_gene = random.randint(0, len(selected_pop)-1)
        candidate_string = string.ascii_letters + string.digits + string.punctuation+ ' '
       # print(selected_pop)
        selected_pop[rand_gene] = random.choice(candidate_string)
        new_population[rand_pop] = ''.join(selected_pop)
       # print(selected_pop)
        mutation_counter += 1
    #print(new_population)
    return new_population

        
            




main()