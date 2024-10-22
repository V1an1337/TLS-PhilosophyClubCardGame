import philosophers, fields, players, effects

CardManager = fields.getField().cardManager


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

    def use(self):
        self.philosopher.addEnergy(self)


class hpCard(basicCard):
    def __init__(self, philosopher: philosophers.basicPhilosopher, hp):
        self.name = "hpCard"
        self.description = f"Give you {hp} hp"
        super().__init__(self.name, self.description, philosopher)
        self.hp = hp

    def use(self):
        self.philosopher.addHP(self.hp)


class basicHandCard(basicCard):
    def __init__(self, name, description, philosopher: philosophers.basicPhilosopher):
        super(basicHandCard, self).__init__(name, description, philosopher)

    def use(self, target):
        self.target = target
        pass
