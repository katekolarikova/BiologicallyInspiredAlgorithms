import math
import numpy as np
import random


class Firefly:
    def __init__(self):
        self.position = []
        self.best_value = 0
        self.light_intensity = 0

    def move(self, other_firefly, lowerLimitX, upperLimitX, lowerLimitY, upperLimitY, func):
        alpha = 0.3
        r = math.sqrt(
            (self.position[0] - other_firefly.position[0]) ** 2 + (self.position[1] - other_firefly.position[1]) ** 2)
        beta = 1 / (1 + r)
        directionX = self.position[0] + beta * r * (other_firefly.position[0] - self.position[0]) + alpha * (
            np.random.normal(0, 1))
        directionY = self.position[1] + beta * r * (other_firefly.position[1] - self.position[1]) + alpha * (
            np.random.normal(0, 1))

        if directionX < lowerLimitX:
            directionX = lowerLimitX
        elif directionX > upperLimitX:
            directionX = upperLimitX

        if directionY < lowerLimitY:
            directionY = lowerLimitY
        elif directionY > upperLimitY:
            directionY = upperLimitY

        self.position = [directionX, directionY]
        self.best_value = func(self.position[0], self.position[1])

    def move_randomly(self, lowerLimitX, upperLimitX, lowerLimitY, upperLimitY, func):
        self.position = [random.uniform(lowerLimitX, upperLimitX), random.uniform(lowerLimitY, upperLimitY)]
        self.best_value = func(self.position[0], self.position[1])


class FireflyAlgo:
    def __init__(self):
        self.pop_size = 30
        self.generation = 300
        self.g_best_value = float('inf')
        self.population = []

    def CreatePopulation(self, lowerLimitX, upperLimitX, lowerLimitY, upperLimitY, func):
        for i in range(self.pop_size):
            firefly = Firefly()
            firefly.position = [random.uniform(lowerLimitX, upperLimitX), random.uniform(lowerLimitY, upperLimitY)]
            firefly.best_value = func(firefly.position[0], firefly.position[1])
            self.population.append(firefly)

    def evaluate_population(self):
        for firefly in self.population:
            if firefly.best_value < self.g_best_value:
                self.g_best_value = firefly.best_value

    def Firefly(self, func, lowerLimitX, upperLimitX, lowerLimitY, upperLimitY):
        self.CreatePopulation(lowerLimitX, upperLimitX, lowerLimitY, upperLimitY, func)
        population_history = []
        self.evaluate_population()

        tmp = []
        for firefly in self.population:
            tmp.append([firefly.position[0], firefly.position[1], func(firefly.position[0], firefly.position[1])])
        population_history.append(tmp)

        t = 0
        while t < self.generation:
            for current_firefly in self.population:
                for other_firefly in self.population:
                    if current_firefly == other_firefly:
                        continue
                    if current_firefly.best_value > other_firefly.best_value:
                        current_firefly.move(other_firefly, lowerLimitX, upperLimitX, lowerLimitY, upperLimitY, func)
                    elif current_firefly.best_value == self.g_best_value:
                        current_firefly.move_randomly(lowerLimitX, upperLimitX, lowerLimitY, upperLimitY, func)

            self.evaluate_population()
            tmp = []
            for firefly in self.population:
                tmp.append([firefly.position[0], firefly.position[1], func(firefly.position[0], firefly.position[1])])
            population_history.append(tmp)
            t += 1

        return population_history
