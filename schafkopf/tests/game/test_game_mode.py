import random

from schafkopf.schafkopf.game.game_modes import GameMode, SOLO, WENZ, PARTNER_MODE, NO_GAME
from schafkopf.schafkopf.game.suits import ALL_SUITS, SUITS_WITHOUT_HEARTS


def test_solo_beats_wenz():
    solo = GameMode(mode=SOLO, suit=random.choice(ALL_SUITS))
    wenz = GameMode(mode=WENZ, suit=None)
    assert solo.beats(wenz)
    assert not wenz.beats(solo)


def test_solo_beats_partner_mode():
    solo = GameMode(mode=SOLO, suit=random.choice(ALL_SUITS))
    partner_game = GameMode(mode=PARTNER_MODE, suit=random.choice(SUITS_WITHOUT_HEARTS))
    assert solo.beats(partner_game)
    assert not partner_game.beats(solo)


def test_solo_beats_no_game():
    solo = GameMode(mode=SOLO, suit=random.choice(ALL_SUITS))
    no_game = GameMode(mode=NO_GAME, suit=None)
    assert solo.beats(no_game)
    assert not no_game.beats(solo)


def test_wenz_beats_partner_mode():
    wenz = GameMode(mode=WENZ, suit=None)
    partner_game = GameMode(mode=PARTNER_MODE, suit=random.choice(SUITS_WITHOUT_HEARTS))
    assert wenz.beats(partner_game)
    assert not partner_game.beats(wenz)


def test_wenz_beats_no_game():
    wenz = GameMode(mode=WENZ, suit=None)
    no_game = GameMode(mode=NO_GAME, suit=None)
    assert wenz.beats(no_game)
    assert not no_game.beats(wenz)


def test_partner_mode_beats_no_game():
    partner_game = GameMode(mode=WENZ, suit=random.choice(SUITS_WITHOUT_HEARTS))
    no_game = GameMode(mode=NO_GAME, suit=None)
    assert partner_game.beats(no_game)
    assert not no_game.beats(partner_game)
