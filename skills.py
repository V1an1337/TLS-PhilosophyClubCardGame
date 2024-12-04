import philosophers
import players, effects, fields, cards


class basicSkill:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def update(self):
        pass


class addHP(basicSkill):
    name = "Add HP"
    description = "Add N HP to a player."

    def __init__(self, philosopher, hp=1):
        super().__init__(self.name, self.description)
        self.hp = hp
        self.philosopher = philosopher

        self.use(self.philosopher)

    def use(self, target):
        target: philosophers.basicPhilosopher
        target.addHP(self.hp)


class loseHP(basicSkill):
    name = "Lose HP"
    description = "Decrease N HP to a player."

    def __init__(self, philosopher, hp=1):
        super().__init__(self.name, self.description)
        self.hp = hp
        self.philosopher = philosopher

        self.use(self.philosopher)

    def use(self, target):
        target: philosophers.basicPhilosopher
        target.loseHP(self.hp)


class addEnergy(basicSkill):  # Add an N-Energy Card to philosopher.
    name = "Add Energy"
    description = "Add a N-Energy Card to a philosopher."

    def __init__(self, philosopher, energy=1):
        super().__init__(self.name, self.description)
        self.energy = energy
        self.philosopher = philosopher

        self.use(self.philosopher)

    def use(self, target):
        target: philosophers.basicPhilosopher
        energyCard = cards.energyCard(target, self.energy)
        energyCard.add()


class attack(basicSkill):
    name = "Attack"
    description = "Attack a player."

    def __init__(self, philosopher, target, damage=1):
        super().__init__(self.name, self.description)
        self.damage = damage
        self.attacker = philosopher
        self.target = target
        self.use(self.target)

    def use(self, target):
        target: philosophers.basicPhilosopher
        loseHP(target, self.damage)
