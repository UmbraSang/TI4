class Tile:

    planets = []
    wormholes = []
    hazards = []
    attackers = []
    defenders = []
    activations = []

    def canActivate(self, race):
        for x in self.activations:
            if x.race == race:
                return False
        return True

    def activated(self, race, fleet):
        self.activations += race
        for x in fleet:
            x.location.exitTile(x)
            x.location = self
            x.location.enterTile(x)
            self.attackers += x

    def enterTile(self, ship):
        # hazards
        for x in self.hazards:
            x.entry(ship)

    def exitTile(self, ship):
        # hazards
        for x in self.hazards:
            x.exit(ship)

    def combatComplete(self):
        if not self.attackers:
            return True
        if not self.defenders:
            self.defenders = self.attackers
            self.attackers = self.getEmptyFleet()
            return True

        return False

    def getEmptyFleet(self):
        emptyFleet = {'owner': None,
                      'flagship': 0,
                      'warsun': 0,
                      'dreadnought': 0,
                      'carrier': 0,
                      'cruiser': 0,
                      'destroyer': 0,
                      }
        return emptyFleet
