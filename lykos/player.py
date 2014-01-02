__author__ = 'alasershark'


class Player:

    def __init__(self, game, user):
        self.game = game
        self.user = user
        self.waiting = False

    def send_message(self, message):
        return NotImplementedError

    def on_message(self, message):
        return NotImplementedError

    def prompt(self, message, with_player_list=True):
        self.send_message(message)
        if with_player_list:
            self.send_message(self.game.player_list)
        self.waiting = True