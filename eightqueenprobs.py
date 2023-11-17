import random
def initialize_population(pop_size, board_size):
    """Initialize a population of random queen placements."""
    population = []
    for _ in range(pop_size):

        placement = random.sample(range(board_size), board_size)
        population.append(placement)
    return population

def fitness(placement):
    """Calculate the fitness of a queen placement. Lower is better."""
    conflicts = 0
    board_size = len(placement)
    for i in range(board_size):
        for j in range(i + 1, board_size):
            if placement[i] == placement[j] or abs(placement[i] - placement[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def select_parents(population, num_parents):
    """Select the top 'num_parents' individuals based on fitness."""
    sorted_population = sorted(population, key=lambda x: fitness(x))
    return sorted_population[:num_parents]

def crossover(parent1, parent2):
    """Perform crossover to create a child."""
    board_size = len(parent1)
    crossover_point = random.randint(1, board_size - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(placement, mutation_rate):
    """Apply mutation to a queen placement."""
    board_size = len(placement)
    for i in range(board_size):
        if random.random() < mutation_rate:
            placement[i] = random.randint(0, board_size - 1)
    return placement

def genetic_algorithm(pop_size, board_size, num_generations, mutation_rate):
    population = initialize_population(pop_size, board_size)
    for generation in range(num_generations):
        parents = select_parents(population, pop_size // 2)
        offspring = []
        while len(offspring) < pop_size:
            parent1, parent2 = random.choices(parents, k=2)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            offspring.append(child)
        population = offspring
        best_placement = min(population, key=lambda x: fitness(x))
        if fitness(best_placement) == 0:
            return best_placement
    return None

if __name__ == "__main__":
    board_size = 8
    pop_size = 100
    num_generations = 1000
    mutation_rate = 0.1
    solution = genetic_algorithm(pop_size, board_size, num_generations, mutation_rate)
    if solution:
        print("Solution found:")
        ans=solution
        print(ans)
    else:
        print("No solution found.")
