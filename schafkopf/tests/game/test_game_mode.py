import random

import pytest

from schafkopf.src.game.game_type import SOLO, WENZ, PARTNER_MODE, NO_GAME
from schafkopf.src.game.game_mode import GameMode, InvalidGameModeException
from schafkopf.src.game.suits import ALL_SUITS, SUITS_WITHOUT_HEARTS, BELLS, HEARTS, LEAVES, ACORNS, NO_SUIT


def test_solo_beats_wenz():
    random_solo = GameMode(game_type=SOLO, suit=random.choice(ALL_SUITS))
    wenz = GameMode(game_type=WENZ, suit=NO_SUIT)
    assert random_solo > wenz
    assert wenz < random_solo


def test_solo_beats_partner_mode():
    random_solo = GameMode(game_type=SOLO, suit=random.choice(ALL_SUITS))
    random_partner_game = GameMode(game_type=PARTNER_MODE, suit=random.choice(SUITS_WITHOUT_HEARTS))
    assert random_solo > random_partner_game
    assert random_partner_game < random_solo


def test_solo_beats_no_game():
    solo = GameMode(game_type=SOLO, suit=random.choice(ALL_SUITS))
    no_game = GameMode(game_type=NO_GAME, suit=NO_SUIT)
    assert solo > no_game
    assert no_game < solo


def test_wenz_beats_partner_mode():
    wenz = GameMode(game_type=WENZ, suit=NO_SUIT)
    partner_game = GameMode(game_type=PARTNER_MODE, suit=random.choice(SUITS_WITHOUT_HEARTS))
    assert wenz > partner_game
    assert partner_game < wenz


def test_wenz_beats_no_game():
    wenz = GameMode(game_type=WENZ, suit=NO_SUIT)
    no_game = GameMode(game_type=NO_GAME, suit=NO_SUIT)
    assert wenz > no_game
    assert no_game < wenz


def test_partner_mode_beats_no_game():
    partner_game = GameMode(game_type=PARTNER_MODE, suit=random.choice(SUITS_WITHOUT_HEARTS))
    no_game = GameMode(game_type=NO_GAME, suit=NO_SUIT)
    assert partner_game > no_game
    assert no_game < partner_game


def test_str_method():
    assert str(GameMode(game_type=SOLO, suit=BELLS)) == "Solo, Bells"
    assert str(GameMode(game_type=SOLO, suit=HEARTS)) == "Solo, Hearts"
    assert str(GameMode(game_type=SOLO, suit=LEAVES)) == "Solo, Leaves"
    assert str(GameMode(game_type=SOLO, suit=ACORNS)) == "Solo, Acorns"
    assert str(GameMode(game_type=WENZ, suit=NO_SUIT)) == "Wenz"
    assert str(GameMode(game_type=PARTNER_MODE, suit=BELLS)) == "Partner mode, Bells"
    assert str(GameMode(game_type=PARTNER_MODE, suit=LEAVES)) == "Partner mode, Leaves"
    assert str(GameMode(game_type=PARTNER_MODE, suit=ACORNS)) == "Partner mode, Acorns"
    assert str(GameMode(game_type=NO_GAME, suit=NO_SUIT)) == "No game"


def test_illegal_suit_for_game_type_raises_exception():
    with pytest.raises(InvalidGameModeException):
        GameMode(game_type=PARTNER_MODE, suit=HEARTS)
    for suit in ALL_SUITS:
        with pytest.raises(InvalidGameModeException):
            GameMode(game_type=WENZ, suit=suit)
        with pytest.raises(InvalidGameModeException):
            GameMode(game_type=NO_GAME, suit=suit)
