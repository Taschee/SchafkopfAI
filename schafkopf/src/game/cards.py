from schafkopf.src.game.ranks import Rank
from schafkopf.src.game.suits import Suit


class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return str(self.rank) + ", " + str(self.suit)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __hash__(self):
        return 10 * self.rank.value + self.suit.value

    def points(self):
        return self.rank.points()
