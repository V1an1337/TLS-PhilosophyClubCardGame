import cards, players, fields


class basicEffect:
    def __init__(self, name, description, player):
        self.name = name
        self.description = description
        self.player = player

    def update(self):
        pass
