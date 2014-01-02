__author__ = 'alasershark'


class Role:

    def __init__(self, game, player):
        self.game = game
        self.player = player

    def on_night(self):
        return NotImplementedError

    def on_day(self):
        return NotImplementedError

    def on_lynch(self):
        return NotImplementedError