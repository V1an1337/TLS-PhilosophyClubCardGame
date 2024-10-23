import philosophers, fields, players, effects

CardManager = fields.getField().getCardManager()


class basicCard:
    def __init__(self, name, description, philosopher: philosophers.basicPhilosopher):
        self.id = CardManager.addCard(self)

        self.name = name
        self.description = description
        self.philosopher = philosopher

    def use(self):
        pass


class energyCard(basicCard):
    def __init__(self, philosopher: philosophers.basicPhilosopher, energy):
        self.name = "energyCard"
        self.description = f"Give you {energy} energy"
        super().__init__(self.name, self.description, philosopher)
        self.energy = energy

    def use(self, target=None):
        if not target:
            target = self.philosopher
        target.addEnergy(self)


class hpCard(basicCard):
    def __init__(self, philosopher: philosophers.basicPhilosopher, hp):
        self.name = "hpCard"
        self.description = f"Give you {hp} hp"
        super().__init__(self.name, self.description, philosopher)
        self.hp = hp

    def use(self, target=None):
        if not target:
            target = self.philosopher
        target.addHP(self.hp)
