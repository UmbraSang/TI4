from Plastic.Ships import WarSun


class Tile:

    systemName = ""
    mapCoordinates = ()  # where in map array tile is
    planets = []  # list of all planets in tile
    wormholes = []  # list of all wormholes in tile
    hazards = []  # list of all hazards on tile

    attackers = []  # list of all invading units
    defenders = []  # list of all local units
    activations = []  # list of all players who have activated the system


    def Tile(self, planets, wormholes, hazards):
        self.planets = planets
        self.wormholes = wormholes
        self.hazards = hazards
        self.__nameSystem()

    def __nameSystem(self):
        for x in self.planets:
            self.systemName += x.name

    def getSystemName(self):
        return self.systemName

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

    def hasWarSun(self):
        testSun = WarSun()
        for x in self.defenders:
            if isinstance(x, testSun):
                return True
        return False
