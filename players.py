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
        if philosopher_type not in philosophers.PhilosopherTypeToPhilosopher:
            raise Exception("Invalid philosopher type")
        if len(self.philosophers) >= 3:
            raise Exception("Too many philosophers")

        newPhilosopher = philosophers.PhilosopherTypeToPhilosopher[philosopher_type](player=self)
        philosopherManager.addPhilosopher(newPhilosopher, self)
        self.philosophers.append(newPhilosopher)
        print(f"Added philosopher {newPhilosopher.id} to {self.name}")
        return newPhilosopher.id

    def getPhilosopher(self, id):
        for philosopher in self.philosophers:
            print(f"{self.name} phil {philosopher.id}",end="")
            if philosopher.id == id:
                return philosopher
        raise Exception("Philosopher not found")


    def addCard(self, card):
        if card in self.cardPile:
            return
        self.cardPile.append(card)

    def haveCard(self, card):
        return card in self.cardPile

    def chooseCardPile(self):
        # This is only a unit test example, not a real implementation
        for i in range(5):
            self.addCard(cards.attackCard)