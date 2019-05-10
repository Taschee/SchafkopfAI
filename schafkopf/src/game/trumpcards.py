from schafkopf.src.game.cards import Card
from schafkopf.src.game.game_type import PARTNER_MODE, WENZ, SOLO
from schafkopf.src.game.ranks import OBER, UNTER, ACE, NINE, EIGHT, TEN, KING, SEVEN
from schafkopf.src.game.suits import ACORNS, HEARTS, LEAVES, BELLS


def trump_cards(self):
    if self.game_type == PARTNER_MODE:
        return [Card(OBER, ACORNS), Card(OBER, LEAVES), Card(OBER, HEARTS), Card(OBER, BELLS),
                Card(UNTER, ACORNS), Card(UNTER, LEAVES), Card(UNTER, HEARTS), Card(UNTER, LEAVES),
                Card(ACE, HEARTS), Card(TEN, HEARTS), Card(KING, HEARTS),
                Card(NINE, HEARTS), Card(EIGHT, HEARTS), Card(SEVEN, HEARTS)]
    elif self.game_type == WENZ:
        return [Card(UNTER, ACORNS), Card(UNTER, LEAVES), Card(UNTER, HEARTS), Card(UNTER, LEAVES)]
    elif self.game_type == SOLO:
        return [Card(OBER, ACORNS), Card(OBER, LEAVES), Card(OBER, HEARTS), Card(OBER, BELLS),
                Card(UNTER, ACORNS), Card(UNTER, LEAVES), Card(UNTER, HEARTS), Card(UNTER, LEAVES),
                Card(ACE, self.suit), Card(TEN, self.suit), Card(KING, self.suit),
                Card(NINE, self.suit), Card(EIGHT, self.suit), Card(SEVEN, self.suit)]
