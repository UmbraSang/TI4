from Plastic.PlanetBound import Planetary


class PDS(Planetary):
    shields = True

    def __init__(self):
        Planetary.__init__(self)
        #
        self.numDice = 1
        self.hit = 6
        #

