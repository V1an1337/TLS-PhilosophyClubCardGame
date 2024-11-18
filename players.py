import philosophers, cards, fields, effects

Field = fields.getField()
cardManager = Field.getCardManager()
philosopherManager = Field.getPhilosopherManager()


class player:
    def __init__(self, name):
        self.name = name
        self.playerID = -1

        self.philosophers = []
        self.cardPile: [cards.basicCard] = []

    def setPlayerID(self, id):
        if self.playerID != -1:  # Already set
            raise Exception("Player ID already set")
        self.playerID = id

    def addPhilosopher(self, philosopher_type):
        if philosopher_type not in philosopherManager.getPhilosopherTypes():
            raise Exception("Invalid philosopher type")
        if len(self.philosophers) >= 3:
            raise Exception("Too many philosophers")

        newPhilosopher = philosophers.PhilosopherTypeToPhilosopher(philosopher_type)()
        philosopherManager.addPhilosopher(newPhilosopher, self)
        self.philosophers.append(newPhilosopher)

    def getPhilosopher(self, id):
        for philosopher in self.philosophers:
            if philosopher.philosopherID == id:
                return philosopher
        raise Exception("Philosopher not found")
#

    def addCard(self, card):
        if card in self.cardPile:
            return
        self.cardPile.append(card)

    def chooseCardPile(self):
        # This is only a unit test example, not a real implementation
        for i in range(5):
            self.addCard(cards.attackCard)

    def chooseCard(self, cardID, philosopher: philosophers.basicPhilosopher, target):
        card = cardManager.getCard(cardID)
        if card not in self.cardPile:
            raise Exception("Card not in pile")

        philosopher.useCard(card, target)
        self.cardPile.remove(card)
