from schafkopf.src.game.game_mode import GameMode
from schafkopf.src.game.ranks import Rank
from schafkopf.src.game.suits import Suit


class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    def points(self):
        return self.rank.points()

    def beats(self, game_mode: GameMode):
        return
