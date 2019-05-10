import random

from schafkopf.src.game.cards import Card
from schafkopf.src.game.ranks import ALL_RANKS, OBER, UNTER, SEVEN, TEN
from schafkopf.src.game.suits import ALL_SUITS, ACORNS, BELLS, HEARTS, LEAVES


class TestCard:
    def test_card_points_are_points_of_rank(self):
        suit = random.choice(ALL_SUITS)
        for rank in ALL_RANKS:
            assert Card(rank, suit).points() == rank.points()

    def test_str_method(self):
        assert str(Card(OBER, ACORNS)) == "Ober, Acorns"
        assert str(Card(UNTER, BELLS)) == "Unter, Bells"
        assert str(Card(SEVEN, HEARTS)) == "Seven, Hearts"
        assert str(Card(TEN, LEAVES)) == "Ten, Leaves"
