import random

from schafkopf.src.game.cards import Card
from schafkopf.src.game.player_hand import PlayerHand
from schafkopf.src.game.ranks import ALL_RANKS
from schafkopf.src.game.suits import ALL_SUITS


class CardDeck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in ALL_RANKS for suit in ALL_SUITS]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_hand(self):
        hand = self.cards[:8]
        self.cards = self.cards[8:]
        return PlayerHand(hand)

    def deal_player_hands(self):
        player_hands = []
        for player in range(4):
            hand = self.deal_hand()
            player_hands.append(hand)
        return player_hands

    def shuffle_and_deal_hands(self):
        self.shuffle()
        return self.deal_player_hands()
