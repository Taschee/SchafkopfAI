from schafkopf.schafkopf.game.suits import ACORNS, BELLS, HEARTS, LEAVES


def test_order_of_suits():
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


def test_str_method():
    assert str(ACORNS) == "Acorns"
    assert str(BELLS) == "Bells"
    assert str(HEARTS) == "Hearts"
    assert str(LEAVES) == "Leaves"