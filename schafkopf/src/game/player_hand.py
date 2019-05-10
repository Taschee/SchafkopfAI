from typing import List

from schafkopf.src.game.cards import Card


class PlayerHand(List[Card]):
    def __init__(self, *args, **kwargs):
        super(PlayerHand, self).__init__(args[0])
