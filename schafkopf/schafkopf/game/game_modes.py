from schafkopf.schafkopf.game.suits import ALL_SUITS, SUITS_WITHOUT_HEARTS


class GameMode:
    def __init__(self, game_type, suit):
        if not self.is_legal(game_type, suit):
            raise InvalidGameModeException("The specified game mode with game type {} and suit {} is not legal"
                                           .format(game_type, suit))
        self.game_type = game_type
        self.suit = suit

    def __gt__(self, other_game_mode):
        return self.game_type > other_game_mode.game_type

    def __lt__(self, other):
        return self.game_type < other.game_type

    def __str__(self):
        if self.game_type in [SOLO, PARTNER_MODE]:
            return str(self.game_type) + ", " + str(self.suit)
        else:
            return str(self.game_type)

    @staticmethod
    def is_legal(mode, suit):
        if mode not in GAME_MODES:
            return False
        if suit not in ALL_SUITS + [None]:
            return False
        if mode == WENZ and suit is not None:
            return False
        if mode == NO_GAME and suit is not None:
            return False
        if mode == PARTNER_MODE and suit not in SUITS_WITHOUT_HEARTS:
            return False
        else:
            return True


class GameType:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if self.value == 0:
            return "No game"
        elif self.value == 1:
            return "Partner mode"
        elif self.value == 2:
            return "Wenz"
        elif self.value == 3:
            return "Solo"

    def __gt__(self, other):
        assert type(other) == GameType, "Cannot compare game type with different object"
        return self.value > other.value

    def __lt__(self, other):
        assert type(other) == GameType, "Cannot compare game type with different object"
        return self.value < other.value


NO_GAME = GameType(0)
PARTNER_MODE = GameType(1)
WENZ = GameType(2)
SOLO = GameType(3)
GAME_MODES = [NO_GAME, PARTNER_MODE, WENZ, SOLO]


class InvalidGameModeException(Exception):
    pass
