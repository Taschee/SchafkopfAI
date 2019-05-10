from schafkopf.src.game.game_type import SOLO, WENZ, PARTNER_MODE, NO_GAME


def test_order_of_game_types():
    assert SOLO > WENZ
    assert SOLO > PARTNER_MODE
    assert SOLO > NO_GAME
    assert WENZ > PARTNER_MODE
    assert WENZ > NO_GAME
    assert PARTNER_MODE > NO_GAME
    assert NO_GAME < SOLO
    assert NO_GAME < WENZ
    assert NO_GAME < PARTNER_MODE
    assert PARTNER_MODE < WENZ
    assert PARTNER_MODE < SOLO
    assert WENZ < SOLO


def test_str_method():
    assert str(SOLO) == "Solo"
    assert str(WENZ) == "Wenz"
    assert str(PARTNER_MODE) == "Partner mode"
    assert str(NO_GAME) == "No game"
