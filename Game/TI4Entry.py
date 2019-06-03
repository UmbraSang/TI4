from Game import Game
from Game import MapBuilder


class TI4Entry:

    gameMap = MapBuilder.buildmap()
    listOfPlayers = getPlayerList()
    gameType = getGameType()
    Game.Game(gameMap, listOfPlayers, gameType)

    def getPlayerList(self):
        playerList = {}
        return playerList

    def getGameType(self):
        return