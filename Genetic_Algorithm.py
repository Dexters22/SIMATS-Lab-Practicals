import random

# -------------------------
# Parameters
# -------------------------
POPULATION_SIZE = 6      # Number of individuals
GENE_LENGTH = 5          # 5 bits to represent numbers 0-31
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.1
GENERATIONS = 10

# -------------------------
# Population Initialization
# -------------------------
def generate_individual():
    return [random.randint(0, 1) for _ in range(GENE_LENGTH)]

def generate_population():
    return [generate_individual() for _ in range(POPULATION_SIZE)]

# -------------------------
# Fitness Function
# -------------------------
def decode(individual):
    """Convert binary list to integer."""
    return sum(bit * (2**idx) for idx, bit in enumerate(reversed(individual)))

def fitness(individual):
    x = decode(individual)
    return x**2

# -------------------------
# Selection (Roulette Wheel)
# -------------------------
def select(population):
    total_fitness = sum(fitness(ind) for ind in population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for ind in population:
        current += fitness(ind)
        if current > pick:
            return ind

# -------------------------
# Crossover
# -------------------------
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, GENE_LENGTH - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    return parent1[:], parent2[:]

# -------------------------
# Mutation
# -------------------------
def mutate(individual):
    for i in range(GENE_LENGTH):
        if random.random() < MUTATION_RATE:
            individual[i] = 1 - individual[i]

# -------------------------
# Genetic Algorithm
# -------------------------
def genetic_algorithm():
    population = generate_population()

    for generation in range(GENERATIONS):
        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent1 = select(population)
            parent2 = select(population)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
        
        population = new_population

        # Print best solution of this generation
        best = max(population, key=fitness)
        print(f"Generation {generation+1}: Best = {decode(best)}, Fitness = {fitness(best)}")

# -------------------------
# Run
# -------------------------
if __name__ == "__main__":
    genetic_algorithm()
