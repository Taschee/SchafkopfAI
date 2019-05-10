from schafkopf.src.game.card_deck import CardDeck
from schafkopf.src.game.player_hand import PlayerHand


class TestPlayerHand:
    def test_in_hand(self):
        card_deck = CardDeck()
        card_deck.shuffle()
        hand = card_deck.deal_hand()
        remaining_cards = card_deck.cards
        player_hand = PlayerHand(hand)

        for card in hand:
            assert card in player_hand
        for card in remaining_cards:
            assert card not in player_hand



