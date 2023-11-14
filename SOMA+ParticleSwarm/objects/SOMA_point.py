class Particle:
    def __init__(self, position, value):
        self.position = position
        self.value = value
        self.type = 'p'


    def getPosition(self, leader , PRT, lowerLimitX, upperLimitX, lowerLimitY, upperLimitY, t):
        tmp = [leader.position[0] - self.position[0], leader.position[1] - self.position[1]]
        tmp = [PRT[0]*tmp[0]*t, PRT[1]*tmp[1]*t]
        final_pos =  [self.position[0]+tmp[0], self.position[1]+tmp[1]]

        if final_pos[0] < lowerLimitX:
            final_pos[0] = lowerLimitX
        elif final_pos[0] > upperLimitX:
            final_pos[0] = upperLimitX

        if final_pos[1] < lowerLimitY:
            final_pos[1] = lowerLimitY
        elif final_pos[1] > upperLimitY:
            final_pos[1] = upperLimitY

        return final_pos
