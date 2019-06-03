class Game:

    map = None
    playerCount = 0
    playerList = {}  # player: playerObject
    turnTracker = None  # order of operations object

    def __init__(self, gameMap, listOfPlayers, gameType):
        self.map = gameMap
        for x in listOfPlayers:
            self.playerList[x] = listOfPlayers[x]
        self.turnTracker = gameType
        