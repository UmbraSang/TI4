import numpy as np


class Map:
    mapArray = None

    def __init__(self, rings):
        side = rings*2+1
        self.mapArray = np.empty((side, side))
        for x in range(rings):
            self.mapArray[x][x] = None
            self.mapArray[side-x][side-x] = None

    def addSystem(self, x, y, system):
        self.mapArray[x][y] = system
        # prompt refresh of displayed map
