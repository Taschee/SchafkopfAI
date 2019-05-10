from schafkopf.src.game.suits import ACORNS, BELLS, HEARTS, LEAVES, NO_SUIT, Suit


class TestSuit:
    def test_order_of_suits(self):
        assert ACORNS > BELLS
        assert ACORNS > HEARTS
        assert ACORNS > LEAVES
        assert LEAVES > HEARTS
        assert LEAVES > BELLS
        assert HEARTS > BELLS
        assert BELLS < ACORNS
        assert HEARTS < ACORNS
        assert LEAVES < ACORNS
        assert HEARTS < LEAVES
        assert BELLS < LEAVES
        assert BELLS < HEARTS
        assert Suit(0) == NO_SUIT
        assert Suit(1) == BELLS
        assert Suit(2) == HEARTS
        assert Suit(3) == LEAVES
        assert Suit(4) == ACORNS

    def test_str_method(self):
        assert str(NO_SUIT) == "No suit"
        assert str(ACORNS) == "Acorns"
        assert str(BELLS) == "Bells"
        assert str(HEARTS) == "Hearts"
        assert str(LEAVES) == "Leaves"
