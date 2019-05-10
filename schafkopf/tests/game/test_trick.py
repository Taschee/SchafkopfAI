import random

import pytest

from schafkopf.src.game.cards import Card
from schafkopf.src.game.ranks import OBER, ACE, SEVEN, EIGHT, NINE, TEN, KING, UNTER, ALL_RANKS
from schafkopf.src.game.suits import ACORNS, BELLS, HEARTS, LEAVES, ALL_SUITS
from schafkopf.src.game.trick import IllegalPlayerIndexException, Trick


class TestTrick:
    def test_initialize_leading_player_index(self):
        illegal_index = random.choice(range(5, 10))
        with pytest.raises(IllegalPlayerIndexException):
            Trick(leading_player_index=illegal_index)

    def test_next_player(self):
        for i in [0, 1, 2]:
            trick = Trick(leading_player_index=i)
            trick.next_player()
            assert trick.current_player_index == i + 1
        trick = Trick(leading_player_index=3)
        trick.next_player()
        assert trick.current_player_index == 0

    def test_trick_points(self):
        trick = Trick(cards=[Card(OBER, ACORNS), Card(ACE, BELLS), None, None])
        assert trick.points() == 14
        trick = Trick(cards=[None, None, None, None])
        assert trick.points() == 0
        trick = Trick(cards=[Card(SEVEN, HEARTS), Card(EIGHT, HEARTS), Card(NINE, HEARTS), Card(SEVEN, LEAVES)])
        assert trick.points() == 0
        trick = Trick(cards=[Card(SEVEN, HEARTS), Card(KING, ACORNS), Card(ACE, HEARTS), Card(TEN, LEAVES)])
        assert trick.points() == 25
        trick = Trick(cards=[None, Card(EIGHT, HEARTS), Card(UNTER, HEARTS), Card(UNTER, ACORNS)])
        assert trick.points() == 4
        cards = [Card(rank=random.choice(ALL_RANKS), suit=random.choice(ALL_SUITS)) for _ in range(4)]
        trick = Trick(cards=cards)
        assert trick.points() == sum([card.points() for card in cards])
