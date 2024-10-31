import philosophers, cards, fields, effects


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

    def addPhilosopher(self, philosopher):
        newPhilosopher = philosopher(self)
        newPhilosopher.setPlayer(self)
        self.philosophers.append(newPhilosopher)

    def addCard(self, card):
        if card in self.cardPile:
            return
        self.cardPile.append(card)

    def chooseCardPile(self):
        # This is only a unit test example, not a real implementation
        for i in range(5):
            self.addCard(cards.attackCard)