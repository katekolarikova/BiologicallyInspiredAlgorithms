import random
def BlindSearch(func, iterationCount,lowerLimitX, upperLimitX, lowerLimitY, upperLimitY):
    # generate first random solution
    maximumValue = func(random.uniform(lowerLimitX, upperLimitX), random.uniform(lowerLimitY, upperLimitY))
    maximumX = None
    maximumY = None
    pointHistory = []
    pointHistory.append((maximumX, maximumY, maximumValue))

    # generate random solutions and compare them with current best solution
    for i in range(iterationCount):
        x = random.uniform(lowerLimitX, upperLimitX)
        y = random.uniform(lowerLimitY, upperLimitY)
        value = func(x, y)
        # if new solution is better than current best solution, update current best solution
        if value < maximumValue:
            maximumValue = value
            maximumX = x
            maximumY = y

            # add current best solution to history of search
            pointHistory.append((maximumX, maximumY, maximumValue))

    return pointHistory
    