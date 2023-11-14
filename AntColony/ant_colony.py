import copy
import math
import random

import numpy as np
from scipy.spatial.distance import pdist, squareform
from City import City

class AntColonyClass:
    def __init__(self, city_numbers):
        self.city_numbers = city_numbers
        self.cities = self.CreateCities(city_numbers, 300)
        self.vaporization_rate = 0.5
        self.pheronome_matrix = [[1 for j in range(city_numbers)] for i in range(city_numbers)]
        self.visibility_matrix = np.linalg.inv(squareform(pdist([self.cities[i].location for i in range(self.city_numbers)], metric='euclidean')))
        self.distance_matrix = squareform(pdist([self.cities[i].location for i in range(self.city_numbers)], metric='euclidean'))


    # set value in visibility matrix of each city to 0 - mark visited city
    def set_visited_city(self, city, cities):
        city_index = city.name
        for i in range( self.city_numbers):
             cities[i][city_index] = 0


    # create cities - random location
    def CreateCities(self, total_city, canvas_size):
        cities = []
        for i in range(total_city):
            tmp_c = City(i, (random.randint(0, canvas_size), random.randint(0, canvas_size)))
            cities.append(tmp_c)
        return cities


    # compute index of next city to visit
    def choose_next_city(self, city, cities):
        probabilities = []

        # cities - visibility matrix for ant
        #t(1,s)^1n(1,s)^2
        for i in range(self.city_numbers):
            if cities[city.name][i] != 0:
                probabilities.append(self.pheronome_matrix[city.name][i] *(cities[city.name][i]**2))
            else:
                probabilities.append(0)

        # probabilities
        sum_probabilities = sum(probabilities)
        probabilities = [p / sum_probabilities if p != 0 else 0 for p in probabilities]

        # cumulative probabilities
        cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]

        # choose next city - find city with probability higher then r
        r = random.uniform(0, 1)
        for i, p in enumerate(cumulative_probabilities):
            # mark cities lower than r
            if r >= p :
                cumulative_probabilities[i] = 0

        # choose next city - find city with probability closest to r and return its index
        max = 2
        index = 0
        for i, p in enumerate(cumulative_probabilities):
            if p < max and p != 0:
                max = p
                index = i

        return index



    # go throw all ants and find the one with best path
    def get_best_path(self, ant_colony):
        best_path = []
        best_distance = float('inf')
        for ant in ant_colony:
            if ant['distance'] < best_distance:
                best_distance = ant['distance']
                best_path = ant['cities']
        return best_path, best_distance


    # update pheromone matrix
    def update_pheromone(self, ant_colony):
        for ant in ant_colony:
            for i in range(self.city_numbers):
                for j in range(self.city_numbers):
                    # formula for updating pheromone matrix
                    self.pheronome_matrix[i][j] = self.pheronome_matrix[i][j] * self.vaporization_rate + 1/ant['distance']


    # compute distance of path
    def get_distance(self, cities):
        distance = 0
        for i in range(len(cities) - 1):
            cityA_name = cities[i].name
            cityB_name = cities[i + 1].name

            cityA = self.cities[cityA_name]
            cityB = self.cities[cityB_name]

            distance += math.sqrt((cityA.location[0] - cityB.location[0]) ** 2 + (cityA.location[1] - cityB.location[1]) ** 2)
        return distance

    def ant_colony(self):
        best_path = []
        best_path_value = float('inf')
        start_city = self.cities[0] # choose start city

        for i in range(90): # pocet iteraci

            # create colony of ants
            ant_colony = [{"cities":[], "distance":0} for k in range(5)]
            # for each ant choose next city
            for ant in ant_colony:
                chosen_city = self.cities[0]

                # add start city to path of ant
                ant['cities'].append(start_city)
                ants_cities = copy.deepcopy(self.visibility_matrix)

                # mark start city as visited
                self.set_visited_city(chosen_city, ants_cities)

                # go throw all cities and create path
                for i in range(self.city_numbers-1):

                    # choose next city
                    next_city_index = self.choose_next_city(chosen_city, ants_cities)
                    next_city = self.cities[next_city_index]
                    ant['cities'].append(next_city)

                    # mark next city as visited
                    self.set_visited_city(next_city, ants_cities)
                    chosen_city = next_city # set next city as current city

                # finish path - add start city to path
                ant['cities'].append(start_city)

            # compute distance of each ant
            for ant in ant_colony:
                distance = self.get_distance(ant['cities'])
                ant['distance'] = distance

            # find best path of all ants
            get_best_path, best_distance = self.get_best_path(ant_colony)

            # if best path is better than previous best path, save it
            if best_distance < best_path_value:
                best_path.append(get_best_path)
                best_path_value = best_distance

            # update pheromone matrix
            self.update_pheromone(ant_colony)

        return best_path

