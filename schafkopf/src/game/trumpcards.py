from schafkopf.src.game.cards import Card
from schafkopf.src.game.game_mode import GameMode
from schafkopf.src.game.game_type import PARTNER_MODE, WENZ, SOLO
from schafkopf.src.game.ranks import OBER, UNTER, ACE, NINE, EIGHT, TEN, KING, SEVEN
from schafkopf.src.game.suits import ACORNS, HEARTS, LEAVES, BELLS


def trump_cards(game_mode: GameMode):
    if game_mode.game_type == PARTNER_MODE:
        return [Card(OBER, ACORNS), Card(OBER, LEAVES), Card(OBER, HEARTS), Card(OBER, BELLS),
                Card(UNTER, ACORNS), Card(UNTER, LEAVES), Card(UNTER, HEARTS), Card(UNTER, LEAVES),
                Card(ACE, HEARTS), Card(TEN, HEARTS), Card(KING, HEARTS),
                Card(NINE, HEARTS), Card(EIGHT, HEARTS), Card(SEVEN, HEARTS)]
    elif game_mode.game_type == WENZ:
        return [Card(UNTER, ACORNS), Card(UNTER, LEAVES), Card(UNTER, HEARTS), Card(UNTER, LEAVES)]
    elif game_mode.game_type == SOLO:
        return [Card(OBER, ACORNS), Card(OBER, LEAVES), Card(OBER, HEARTS), Card(OBER, BELLS),
                Card(UNTER, ACORNS), Card(UNTER, LEAVES), Card(UNTER, HEARTS), Card(UNTER, LEAVES),
                Card(ACE, game_mode.suit), Card(TEN, game_mode.suit), Card(KING, game_mode.suit),
                Card(NINE, game_mode.suit), Card(EIGHT, game_mode.suit), Card(SEVEN, game_mode.suit)]
