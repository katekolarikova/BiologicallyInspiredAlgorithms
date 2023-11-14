import random
import numpy as np
from objects.SOMA_point import Particle


class SOMA_all_to_one:
    def __init__(self):
        self.pop_size = 10
        self.M_max = 100
        self.PRT = 0.4
        self.path_length = 3.0
        self.step = 0.11
        self.population = []
        self.leader = None

    def CreatePopulation(self, lowerLimitX, upperLimitX, lowerLimitY, upperLimitY, func):
        for i in range(self.pop_size):

            position = [random.uniform(lowerLimitX, upperLimitX), random.uniform(lowerLimitY, upperLimitY)]

            value = func(position[0], position[1])
            particle = Particle(position, value)
            self.population.append(particle)

    def GetBestFromPop(self):
        best_particle = self.population[0]
        for particle in  self.population:
            if particle.type == 'l':
                particle.type = 'p'
            if particle.value < best_particle.value:
                best_particle = particle
        best_particle.type = 'l'
        return best_particle

    def getPRT(self, particle):
        new_prt_vec = [0,0]
        #dierction should not be null
        while new_prt_vec[0] == 0 and new_prt_vec[1] == 0:
            for i in range(2):
                if np.random.uniform() < self.PRT:
                    new_prt_vec[i] = 1
        return new_prt_vec

    def SOMA(self,func, lowerLimitX, upperLimitX, lowerLimitY, upperLimitY):
        self.CreatePopulation(lowerLimitX, upperLimitX, lowerLimitY, upperLimitY, func)
        m = 0
        point_history = []
        population_history = []

        self.leader = self.GetBestFromPop()


        point_history.append([  self.leader.position[0],   self.leader.position[1],   self.leader.value])
        # iterations
        while m < self.M_max:
            # for each individual in population
            for i, particle in enumerate(self.population):
                t = 0
                point_best_value = float('inf')
                point_best_position = None

                while t < self.path_length:
                    # do not calculate for leader
                    if particle.type != 'l':

                        new_pos = particle.getPosition(self.leader, self.getPRT(particle), lowerLimitX, upperLimitX,
                                                       lowerLimitY, upperLimitY, t)
                        new_value = func(new_pos[0], new_pos[1])
                        if new_value < particle.value:
                            point_best_position = new_pos
                            point_best_value= new_value
                    t+=self.step
                particle.value = point_best_value if point_best_value != float('inf') else particle.value
                particle.position = point_best_position if point_best_position is not None else particle.position

            self.leader = self.GetBestFromPop()
            tmp = []
            for particle  in self.population:
                tmp.append([particle.position[0], particle.position[1], particle.value, particle.type])
            population_history.append(tmp)


            m += 1

        return population_history
