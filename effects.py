import cards, players, fields
import philosophers


class basicEffect:
    def __init__(self, name, description, philosopher: philosophers.basicPhilosopher):
        self.name = name
        self.description = description
        self.philosopher = philosopher

        self.dead = False

    def update(self):
        pass

    def destroy(self):
        self.dead = True


class healEffect(basicEffect):
    def __init__(self, player, amount, duration):  # player 永远放在参数第一位
        self.name = "healEffect"
        self.description = f"Heals the player for {amount} health for {duration} turns"
        super().__init__(self.name, self.description, player)
        self.amount = amount
        self.duration = duration
        self.turnsLeft = duration

    def update(self):
        if self.turnsLeft:
            self.philosopher.addHP(self.amount)
            self.turnsLeft -= 1
        else:
            self.destroy()
