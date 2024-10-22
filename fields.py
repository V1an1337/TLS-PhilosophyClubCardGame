import cards
import philosophers


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
        self.cardPile: [cards.basicCard] = []
        self.graveYard: [cards.basicCard] = []
        self.cardManager = cardManager()


Field = field()


def getField() -> field:
    return Field


def setField(f):
    global Field
    Field = f
