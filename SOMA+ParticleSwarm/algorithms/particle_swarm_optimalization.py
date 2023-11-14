import random
from objects.swarm import Swarm
class SwarmOptimalization:
    def __init__(self):
        self.pop_size = 30
        self.M_max = 30
        self.c1 = 2
        self.c2 = 2
        self.v_mini, self.v_maxi = -1, 1
        self.g_best = [0, 0, 0]
        self.population = []

    def CreatePopulation(self, lowerLimitX, upperLimitX, lowerLimitY, upperLimitY, func):
        for i in range(self.pop_size):
            swarm = Swarm()
            swarm.position = [random.uniform(lowerLimitX, upperLimitX), random.uniform(lowerLimitY, upperLimitY)]
            swarm.velocity = [0,0]
            swarm.best_position = swarm.position
            swarm.best_value = func(swarm.position[0], swarm.position[1])
            self.population.append(swarm)

    def GetBestFromPop(self):
        best_swarm = self.population[0]
        for swarm in self.population:
            if swarm.best_value < best_swarm.best_value:
                best_swarm = swarm
        return best_swarm

    def ParticleSwarmOptimalization(self,func, lowerLimitX, upperLimitX, lowerLimitY, upperLimitY):
        self.CreatePopulation(lowerLimitX, upperLimitX, lowerLimitY, upperLimitY, func)
        m = 0
        point_history = []
        population_history = []

        self.g_best = self.GetBestFromPop().best_position

        for i, swarm in enumerate(self.population):
            swarm.GenerateVector(self.c1, self.c2, self.g_best, 0, self.M_max)

        point_history.append([self.g_best[0], self.g_best[1], func(self.g_best[0], self.g_best[1])])
        # iterations
        while m < self.M_max:
            # for each individual in population
            for i, swarm in enumerate(self.population):

                #compute new position and velocity
                swarm.GenerateVector(self.c1, self.c2, self.g_best, i, self.M_max)
                swarm.GeneratePosition( lowerLimitX, upperLimitX, lowerLimitY, upperLimitY)

                # update best position and value for particle
                value = func(swarm.position[0], swarm.position[1])
                if value < swarm.best_value:
                    swarm.best_position = swarm.position
                    swarm.best_value = value
                    best_value = func(self.g_best[0], self.g_best[1])

                    # update global best position and value
                    if value < best_value:
                        self.g_best = swarm.position
                        point_history.append([self.g_best[0], self.g_best[1], best_value])
                        tmp = []

                        # update population history
                        for swarm in self.population:
                             tmp.append([swarm.position[0], swarm.position[1], func(swarm.position[0], swarm.position[1])])
                        population_history.append(tmp)

            m += 1

        return population_history
