from Plastic.PlanetBound import Planetary


class SpaceDock(Planetary):
    def __init__(self):
        Planetary.__init__(self)
        #
        self.capacity = 3
        self.production = self.location.resource+3
        #
