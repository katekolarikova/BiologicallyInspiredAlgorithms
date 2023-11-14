import copy
import random

def GeneratePopulation(NP, lowerLimitX, upperLimitX, lowerLimitY, upperLimitY, func):
    pop = []
    for i in range(NP):
        x = random.uniform(lowerLimitX, upperLimitX)
        y = random.uniform(lowerLimitY, upperLimitY)
        pop.append([x, y, func(x, y)])
    return pop

def GetBestPoint(population):
    best_point = population[0]
    best_value = best_point[2]
    for point in population:
        value = point[2]
        if value < best_value:
            best_value = value
            best_point = point
    return best_point

def GetVVector(x_r1, x_r2, x_r3, F):
    result = [x - y for x, y in zip(x_r1, x_r2)]
    result = [x * F for x in result]
    v = [x + y for x, y in zip(result, x_r3)]

    return v

def DifferentialEvolution(func, lowerLimitX, upperLimitX, lowerLimitY, upperLimitY):
    g_max = 20  # generation count
    F = 0.5  # mutatioan factor
    CR = 0.5
    NP = 10  # size of population
    point_history = []

    pop = GeneratePopulation(NP, lowerLimitX, upperLimitX, lowerLimitY, upperLimitY, func)
    g = 0

    # generation iteration
    while g < g_max:
        new_pop = copy.deepcopy(pop)

        # for each individual in population
        for i, x in enumerate(pop):

            # select 3 random individuals
            r1, r2, r3 = random.sample(range(1, NP), 3)

            # compute v and u vector
            x_r1, x_r2, x_r3 = pop[r1], pop[r2], pop[r3]
            v = GetVVector(x_r1, x_r2, x_r3, F)
            u = [0, 0, 0]

            j_rnd = random.randint(0, 2)

            # compute u vector
            for j in range(2):
                if random.random() < CR or j == j_rnd:
                    u[j] = v[j]
                else:
                    u[j] = x[j]

            u[2] = func(u[0], u[1])

            # select better point
            if u[2] < x[2]:
                new_pop[i] = u

            pop = new_pop
            current_best_point = GetBestPoint(pop)
            point_history.append(current_best_point)
        g += 1

    return point_history
