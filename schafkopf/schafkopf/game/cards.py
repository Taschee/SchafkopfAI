from schafkopf.schafkopf.game.ranks import ALL_RANKS
from schafkopf.schafkopf.game.suits import ALL_SUITS


class Card:
    def __init__(self, rank, suit):
        if not self.is_legal(rank, suit):
            raise InvalidCardDefinitionException("Invalid rank {} or suit {} for card definition".format(rank, suit))
        self.rank = rank
        self.suit = suit

    def beats(self, game_mode):
        return

    @staticmethod
    def is_legal(rank, suit):
        if rank not in ALL_RANKS or suit not in ALL_SUITS:
            return False
        else:
            return True


class InvalidCardDefinitionException(Exception):
    pass
