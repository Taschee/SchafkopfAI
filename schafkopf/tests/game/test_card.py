import random

from schafkopf.src.game.cards import Card
from schafkopf.src.game.ranks import ALL_RANKS
from schafkopf.src.game.suits import ALL_SUITS


class TestCard:
    def test_card_points_are_points_of_rank(self):
        suit = random.choice(ALL_SUITS)
        for rank in ALL_RANKS:
            assert Card(rank, suit).points() == rank.points()
