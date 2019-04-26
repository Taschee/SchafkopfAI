NO_GAME = 0
PARTNER_MODE = 1
WENZ = 2
SOLO = 3


class GameMode:
    def __init__(self, mode, suit):
        self.mode = mode
        self.suit = suit

    def beats(self, other_game_mode):
        return self.mode > other_game_mode.mode
