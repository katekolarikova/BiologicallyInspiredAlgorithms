import numpy as np
from numpy import random


def generate_neighbours(x, y, distance, lowerLimit, upperLimit, st_dev_x=2, st_dev_y=2):

    new_x = np.random.normal(loc=x, scale=st_dev_x, size=None)
    new_y = np.random.normal(loc=y, scale=st_dev_y, size=None)

    # check boundaries
    if new_x < lowerLimit:
        new_x = lowerLimit
    elif new_x > upperLimit:
        new_x = upperLimit

    if new_y < lowerLimit:
        new_y = lowerLimit
    elif new_y > upperLimit:
        new_y = upperLimit

    return new_x, new_y



def simulated_annealing(func, iterationCount, lowerLimitX, upperLimitX, lowerLimitY, upperLimitY, st_dev_x, st_dev_y):
    # generate first random solution
    currentX = random.uniform(lowerLimitX, upperLimitX)
    currentY = random.uniform(lowerLimitY, upperLimitY)
    bestX = currentX
    bestY = currentY

    current_energy = func(currentX, currentY)
    best_energy = current_energy
    temperature = 100
    coolingRate = 0.5 # cim vetsi, tim pomalejsi ochlazovani, tedy vetsi pravdepodobnost spravneho reseni

    pointHistory = []
    pointHistory.append((currentX, currentY, current_energy))

    # algorithm continue till given temperature limit
    while temperature > 0:
        # kolikkrat chci opakovat zihani v ramci jednoho ochlazovani
        for i in range(iterationCount):
            # generate random solutions and compare them with current best solution
            x, y = generate_neighbours(currentX, currentY, 3, lowerLimitX, upperLimitX)
            new_energy = func(x, y)
            energy_difference = new_energy - current_energy
            if energy_difference < 0:
                currentX = x
                currentY = y
                current_energy = new_energy
                pointHistory.append((currentX, currentY, current_energy))
                if current_energy < best_energy: # we found a better solution
                    bestX = currentX
                    bestY = currentY
                    best_energy = current_energy

            # solution is accepted with propability
            else:
                probability = round(np.exp(np.float128(-energy_difference) /np.float128( temperature)))
                # vyhneme se lokalnim
                # with decreasing temperature, probability of accepting worse solution decreases
                if probability > random.uniform(0, 1): # accept solution if randomly generated number is lower
                    currentX = x
                    currentY = y
                    current_energy = new_energy
                    pointHistory.append((currentX, currentY, current_energy))

                # add current best solution to history of search
        temperature *= coolingRate
    return pointHistory