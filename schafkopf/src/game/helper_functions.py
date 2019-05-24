from typing import Optional, List

from schafkopf.src.game.cards import Card
from schafkopf.src.game.game_mode import GameMode
from schafkopf.src.game.game_type import PARTNER_MODE, WENZ, SOLO
from schafkopf.src.game.ranks import OBER, UNTER, ACE, NINE, EIGHT, TEN, KING, SEVEN, ALL_RANKS
from schafkopf.src.game.suits import ACORNS, HEARTS, LEAVES, BELLS, ALL_SUITS


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


def sorted_hand(hand: List[Card], game_mode: Optional[GameMode]):
    if game_mode is None:
        trumpcards = trump_cards(GameMode(PARTNER_MODE, BELLS))
    else:
        trumpcards = trump_cards(game_mode)
    trumps_in_hand = [trump for trump in trumpcards if trump in hand]
    bells = [Card(rank, BELLS) for rank in ALL_RANKS if (rank, BELLS) in hand and (rank, BELLS) not in trumpcards]
    hearts = [Card(rank, HEARTS) for rank in ALL_RANKS if
              (rank, HEARTS) in hand and (rank, HEARTS) not in trumpcards]
    leaves = [Card(rank, LEAVES) for rank in ALL_RANKS if
              (rank, LEAVES) in hand and (rank, LEAVES) not in trumpcards]
    acorns = [Card(rank, ACORNS) for rank in ALL_RANKS if
              (rank, ACORNS) in hand and (rank, ACORNS) not in trumpcards]
    sorted_hand = trumps_in_hand + acorns + leaves + hearts + bells
    return sorted_hand
