from schafkopf.src.game.game_type import PARTNER_MODE, WENZ, SOLO, GAME_MODES, NO_GAME, GameType
from schafkopf.src.game.suits import ALL_SUITS, SUITS_WITHOUT_HEARTS, Suit, NO_SUIT


class GameMode:
    def __init__(self, game_type: GameType, suit: Suit):
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
        if suit not in ALL_SUITS + [NO_SUIT]:
            return False
        if mode == WENZ and suit != NO_SUIT:
            return False
        if mode == NO_GAME and suit != NO_SUIT:
            return False
        if mode == PARTNER_MODE and suit not in SUITS_WITHOUT_HEARTS:
            return False
        else:
            return True


class InvalidGameModeException(Exception):
    pass
