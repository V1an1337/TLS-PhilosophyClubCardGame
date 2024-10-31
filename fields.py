import cards
import philosophers
import players


class CustomError(Exception):
    def __init__(self, message, details=None):
        self.message = message
        super().__init__(message)
        self.details = details

class cardManager:
    def __init__(self):
        self.cardID = 0
        self.cards = []

    def __getCardID(self):
        self.cardID += 1
        return self.cardID

    def addCard(self, card) -> int:
        self.cards.append(card)
        return self.__getCardID()

    def getCard(self, id):
        return self.cards[id - 1]  # id is 1-indexed


class field:
    def __init__(self):
        self.state = 0  # [0: setup, 1: normal, -1: error]
        self.cardPile: [cards.basicCard] = []
        self.graveYard: [cards.basicCard] = []
        self.cardManager = cardManager()

        self.playerID = 0
        self.players = []

    def startGame(self):
        if self.state != 0:
            return False, "Game already started"
        if len(self.getPlayers()) < 2:
            return False, "Not enough players"

        self.state = 1
        return True, self.state

    def __getPlayerID(self):
        self.playerID += 1
        return self.playerID

    def addPlayer(self, name):
        if self.state != 0:
            return False, "Game already started"

        player = players.player(name)
        player_id = self.__getPlayerID()
        player.playerID = player_id

        self.players.append(player)
        return True, player_id

    def getPlayer(self, id):
        return self.players[id - 1]  # id is 1-indexed

    def getPlayers(self):
        return self.players

    def getCardManager(self):
        return self.cardManager


Field = field()


def getField() -> field:
    return Field


def setField(f):
    global Field
    Field = f
