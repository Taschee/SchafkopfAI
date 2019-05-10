from schafkopf.src.game.game_mode import GameMode
from schafkopf.src.game.ranks import ALL_RANKS, Rank
from schafkopf.src.game.suits import ALL_SUITS, Suit


class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    def beats(self, game_mode: GameMode):
        return


