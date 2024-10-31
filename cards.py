import philosophers, fields, players, effects, skills

CardManager = fields.getField().getCardManager()


class basicCard:
    def __init__(self, name, description, cost: int):
        self.id = CardManager.addCard(self)

        self.name = name
        self.description = description
        self.cost = cost  # 耗费一张能量值为n的能量卡

    def use(self, attacker, target):
        pass


class energyCard(basicCard):
    name = "Energy Card"
    description = f"Give you N energy"
    cost = 0

    def __init__(self, philosopher, energy):  # philosopher 永远放在参数第一位, player同理

        super().__init__(self.name, self.description, self.cost)
        self.energy = energy
        self.philosopher = philosopher

    def use(self, target=None):  # Add Energy card to philosopher
        if not target:
            target = self.philosopher
        target.addEnergy(self)


class hpCard(basicCard):
    name = "HP Card"
    description = f"Give you N hp"
    cost = 1

    def __init__(self, hp):
        super().__init__(self.name, self.description, self.cost)
        self.hp = hp

    def use(self, attacker, target=None):
        if not target:
            target = attacker
        skills.addHP(target)


class attackCard(basicCard):
    name = "Attack Card"
    description = f"Attack a player"
    cost = 1

    def __init__(self):
        super().__init__(self.name, self.description, self.cost)

    def use(self, attacker, target):
        skills.attack(attacker, target)


class healCard(basicCard):
    name = "Heal Card"
    description = f"Give a 3-rounds heal effect to a player"
    cost = 1

    def __init__(self):
        super().__init__(self.name, self.description, self.cost)

    def use(self, attacker, target=None):
        if not target:
            target = attacker
        effect = effects.healEffect(target, 1, 3)
        target.addEffect(effect)
