from schafkopf.schafkopf.game.ranks import SEVEN, EIGHT, NINE, TEN, UNTER, OBER, KING, ACE, ALL_RANKS


def test_str_method():
    assert str(SEVEN) == "Seven"
    assert str(EIGHT) == "Eight"
    assert str(NINE) == "Nine"
    assert str(TEN) == "Ten"
    assert str(UNTER) == "Unter"
    assert str(OBER) == "Ober"
    assert str(KING) == "King"
    assert str(ACE) == "Ace"


def test_order_of_ranks():
    for rank in [rank for rank in ALL_RANKS if rank != SEVEN]:
        assert SEVEN < rank
        assert not SEVEN > rank
    for rank in [rank for rank in ALL_RANKS if rank not in [SEVEN, EIGHT]]:
        assert EIGHT < rank
        assert not EIGHT > rank
    for rank in [rank for rank in ALL_RANKS if rank not in [SEVEN, EIGHT, NINE]]:
        assert NINE < rank
        assert not NINE > rank
    for rank in [rank for rank in ALL_RANKS if rank not in [SEVEN, EIGHT, NINE, UNTER]]:
        assert UNTER < rank
        assert not UNTER > rank
    for rank in [KING, TEN, ACE]:
        assert OBER < rank
        assert not OBER > rank
    for rank in [TEN, ACE]:
        assert KING < rank
        assert not KING > rank
    assert TEN < ACE
    assert not TEN > ACE
    for rank in ALL_RANKS:
        assert not rank > rank
        assert not rank < rank


def test_point_value_of_ranks():
    assert ACE.points() == 11
    assert TEN.points() == 10
    assert KING.points() == 4
    assert OBER.points() == 3
    assert UNTER.points() == 2
    assert NINE.points() == 0
    assert EIGHT.points() == 0
    assert SEVEN.points() == 0
