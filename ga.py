import random
from solver import bfs_solve

ROWS, COLS = 10, 10


# Create a single random map
def create_map():
    grid = [['.' for _ in range(COLS)] for _ in range(ROWS)]

    for i in range(ROWS):
        for j in range(COLS):
            if random.random() < 0.3:
                grid[i][j] = '#'

    # Start and End
    grid[0][0] = 'S'
    grid[ROWS-1][COLS-1] = 'E'

    return grid


# Create initial population
def create_population(n):
    return [create_map() for _ in range(n)]


# Fitness function
def fitness(grid):
    solvable, path_len = bfs_solve(grid)

    # Strong penalty for unsolvable maps
    if not solvable:
        return -10000

    return path_len


# Select best maps
def select_best(population):
    return sorted(population, key=fitness, reverse=True)[:5]


# Crossover
def crossover(p1, p2):
    child = []

    for r in range(ROWS):
        row = []
        for c in range(COLS):
            if random.random() < 0.5:
                row.append(p1[r][c])
            else:
                row.append(p2[r][c])
        child.append(row)

    # Ensure start and end
    child[0][0] = 'S'
    child[ROWS-1][COLS-1] = 'E'

    return child


# Mutation
def mutate(grid):
    for r in range(ROWS):
        for c in range(COLS):
            if random.random() < 0.05:
                if grid[r][c] == '.':
                    grid[r][c] = '#'
                elif grid[r][c] == '#':
                    grid[r][c] = '.'

    # Ensure start and end remain fixed
    grid[0][0] = 'S'
    grid[ROWS-1][COLS-1] = 'E'

    return grid



# Generate SOLVABLE grid (FINAL)
def generate_solvable_grid():
    while True:
        population = create_population(20)

        valid_maps = []

        for g in population:
            solvable, path_len = bfs_solve(g)
            if solvable:
                valid_maps.append((g, path_len))

        # If at least one valid map found
        if valid_maps:
            # Sort by path length (harder maps preferred)
            valid_maps.sort(key=lambda x: x[1], reverse=True)

            return valid_maps[0][0]