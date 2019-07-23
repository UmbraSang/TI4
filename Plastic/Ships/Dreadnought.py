from Plastic.Ships import SustainClass


class Dreadnought(SustainClass):

    def __init__(self):
        SustainClass.__init__(self)
        # TODO: Refactor into visitor for unit upgrades?
        self.cost = 4
        self.numDice = 1
        self.hit = 5
        self.capacity = 1
        self.production = 0
        self.move = 1

        self.canBombard = True
        #


