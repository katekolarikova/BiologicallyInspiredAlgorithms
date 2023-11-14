import random

import numpy as np

# generates random neighbours for given point in given distance (standart deviation)
def generate_neighbours(x, y, distance, lowerLimit, upperLimit, st_dev_x=1, st_dev_y=1):

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



def HillClimbing(func, iterationCount, lowerLimitX, upperLimitX, lowerLimitY, upperLimitY, st_dev_x, st_dev_y):
    # generate first random solution
    maximumX = random.uniform(lowerLimitX, upperLimitX)
    maximumY = random.uniform(lowerLimitY, upperLimitY)
    maximumValue = func(maximumX, maximumY)

    pointHistory = []
    pointHistory.append((maximumX, maximumY, maximumValue))

    # generate random solutions and compare them with current best solution
    for i in range(iterationCount):
        x, y = generate_neighbours(maximumX, maximumY, 3, lowerLimitX, upperLimitX)

        value = func(x, y)
        # if new solution is better than current best solution, update current best solution
        if value < maximumValue:
            maximumValue = value
            maximumX = x
            maximumY = y

            # add current best solution to history of search
            pointHistory.append((maximumX, maximumY, maximumValue))

    return pointHistory
