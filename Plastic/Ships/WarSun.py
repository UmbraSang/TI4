from Plastic.Ships import SustainClass


class WarSun(SustainClass):

    def __init__(self):
        SustainClass.__init__(self)
        # TODO: Refactor into visitor for unit upgrades?
        self.cost = 12
        self.numDice = 3
        self.hit = 3
        self.capacity = 6
        self.production = 0
        self.move = 2

        self.canBombard = True
        #
