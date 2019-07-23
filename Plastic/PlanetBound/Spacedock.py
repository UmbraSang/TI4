from Plastic.PlanetBound import Planetary


class SpaceDock(Planetary):
    def __init__(self):
        Planetary.__init__(self)
        #
        self.capacity = 3
        self.production = 3
        #

    def getBaseProduction(self):
        return self.production

    def getProductionLimit(self):
        return self.location.productionLimit()
