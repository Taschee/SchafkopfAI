from typing import List, Optional

from schafkopf.src.game.cards import Card
from schafkopf.src.game.game_mode import GameMode
from schafkopf.src.game.game_type import PARTNER_MODE
from schafkopf.src.game.helper_functions import trump_cards
from schafkopf.src.game.ranks import ALL_RANKS
from schafkopf.src.game.suits import BELLS, HEARTS, LEAVES, ACORNS


class PlayerHand(List[Card]):
    def __init__(self, cards):
        super(PlayerHand, self).__init__(cards)

    def sorted_hand(self, game_mode: Optional[GameMode]):
        if game_mode is None:
            trumpcards = trump_cards(GameMode(PARTNER_MODE, BELLS))
        else:
            trumpcards = trump_cards(game_mode)
        trumps_in_hand = [trump for trump in trumpcards if trump in self]
        bells = [Card(rank, BELLS) for rank in ALL_RANKS if (rank, BELLS) in self and (rank, BELLS) not in trumpcards]
        hearts = [Card(rank, HEARTS) for rank in ALL_RANKS if
                  (rank, HEARTS) in self and (rank, HEARTS) not in trumpcards]
        leaves = [Card(rank, LEAVES) for rank in ALL_RANKS if
                  (rank, LEAVES) in self and (rank, LEAVES) not in trumpcards]
        acorns = [Card(rank, ACORNS) for rank in ALL_RANKS if
                  (rank, ACORNS) in self and (rank, ACORNS) not in trumpcards]
        sorted_hand = trumps_in_hand + acorns + leaves + hearts + bells
        return sorted_hand

