import random
class Swarm:
    def __init__(self):
        self.position = []
        self.velocity = []
        self.best_position = []
        self.best_value = 0

    def GenerateVector(self, c1, c2, g_best, i, M_max):
        rand1 = random.random()

        new_swarm_velocity = []
        w=0.9 - 0.5*i/M_max
        for i in range(2):
            new_velocity =  w * self.velocity[i] + c1 * rand1 * (self.best_position[i] - self.position[i]) + c2 * rand1 * (g_best[i] - self.position[i])
            new_swarm_velocity.append(new_velocity)

        self.velocity = new_swarm_velocity

    def GeneratePosition(self, lowerLimitX, upperLimitX, lowerLimitY, upperLimitY):
        rand1 = random.random()

        new_swarm_position = []

        for i in range(2):
            new_position = self.position[i] + self.velocity[i]
            new_swarm_position.append(new_position)

        # check if new position is in range
        if new_swarm_position[0] < lowerLimitX:
            new_swarm_position[0] = lowerLimitX
        elif new_swarm_position[0] > upperLimitX:
            new_swarm_position[0] = upperLimitX

        if new_swarm_position[1] < lowerLimitY:
            new_swarm_position[1] = lowerLimitY
        elif new_swarm_position[1] > upperLimitY:
            new_swarm_position[1] = upperLimitY

        self.position = new_swarm_position
