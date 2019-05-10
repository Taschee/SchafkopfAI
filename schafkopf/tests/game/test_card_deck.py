from typing import Set

from schafkopf.src.game.card_deck import CardDeck
from schafkopf.src.game.cards import Card
from schafkopf.src.game.ranks import ALL_RANKS
from schafkopf.src.game.suits import ALL_SUITS


class TestCardDeck:
    def test_number_of_dealt_cards(self):
        player_hands = CardDeck().shuffle_and_deal_hands()
        assert len(player_hands) == 4
        for i in range(3):
            assert len(player_hands[i]) == 8

    def test_all_cards_are_dealt(self):
        expected_cards = [Card(rank, suit) for rank in ALL_RANKS for suit in ALL_SUITS]

        player_hands = CardDeck().shuffle_and_deal_hands()

        actual_cards = [card for hand in player_hands for card in hand]

        assert len(actual_cards) == len(expected_cards)
        for card in actual_cards:
            assert card in expected_cards



