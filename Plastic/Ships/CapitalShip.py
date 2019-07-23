from Plastic import Unit


class CapitalShip(Unit):
    move = 1

    def __init__(self):
        Unit.__init__(self)

    def bombardPlanet(self):
        if self.canBombard:
            for x in range(self.numDice):
                # choose target
                target = 0
                if self.roll() >= self.hit:
                    self.location.planets[target].receiveBombard()
