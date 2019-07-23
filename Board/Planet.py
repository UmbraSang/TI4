class Planet:
    __planetName = ""
    __parentSystem = None
    __resourceValue = 0
    __influenceValue = 0
    __traitType = None
    __techType = None

    __owner = None
    __defenders = ()
    __numPDS = 0
    pdsLimit = 2  # TODO: store value in global object?
    __spaceDock = None

    def Planet(self, planetName, parentSystem, resourceValue, influenceValue, traitType, techType):
        self.__planetName = planetName
        self.__parentSystem = parentSystem
        self.__resourceValue = resourceValue
        self.__influenceValue = influenceValue
        self.__traitType = traitType
        self.__techType = techType

    def hasPDS(self):
        if self.numPDS != 0:
            return True
        return False

    def hasSpaceDock(self):
        if self.spaceDock is not None:
            return True

    def __changeHands(self, conquerors):
        self.owner = conquerors[0].owner
        # Todo: lizix
        self.spaceDock = None
        self.numPDS = None
        self.defenders = conquerors

    def groundForceLanding(self, invaders):
        if invaders[0].owner != self.owner:
            victors = groundCombat(invaders, self.defenders)  # TODO: implement battle machine
            if self.owner != victors[0].owner:
                self.__changeHands(victors)
        else:
            self.defenders.amend(invaders)

    def numInfantry(self):
        return len(self.defenders)

    def receiveBombard(self, bombardSuccesses):
        if self.hasPDS() and not self.__parentSystem.hasWarSun():
            print("bombard blocked")
        else:
            for x in range(bombardSuccesses):
                self.defenders[0].death()

    def placePDS(self):
        if self.numPDS != self.pdsLimit:
            self.numPDS += 1
        else:
            print("planet full. PDS placement blocked.")

    def placeSpaceDock(self, newSpaceDock):
        if not self.hasSpaceDock():
            self.__spaceDock = newSpaceDock
        else:
            print("Spacedock Already Exists!!")

    def productionLimit(self):
        return self.resourceValue + self.spaceDock.production
