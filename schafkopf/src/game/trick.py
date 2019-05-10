from typing import List, Optional

from schafkopf.src.game.cards import Card


class Trick:
    def __init__(self, leading_player_index: int = 0, cards: List[Optional[Card]] = ()):
        if cards:
            assert len(cards) == 4, "Only possible to initialize a trick with 4 cards"
            self.cards = cards
        else:
            self.cards = [None for _ in range(4)]
        if leading_player_index not in [0, 1, 2, 3]:
            raise IllegalPlayerIndexException("Leading player index {} is not possible".format(leading_player_index))
        self.winner = None
        self.leading_player_index = leading_player_index
        self.current_player_index = leading_player_index
        self.num_cards = 0
        self.initialize_cards_and_current_player(cards)

    def __str__(self):
        return str(self.cards)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def initialize_cards_and_current_player(self, cards):
        for card in cards:
            if card is not None:
                self.next_player()
                self.num_cards += 1

    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % 4

    def points(self):
        points = 0
        for card in self.cards:
            if card is not None:
                points += card.points()
        return points

    def determine_trickwinner(self, trumpcards):
        # determines index of winning card / player
        trumps_in_trick = [card for card in self.cards if card in trumpcards]
        if len(trumps_in_trick) > 0:
            best_trump = min([trumpcards.index(trump) for trump in trumps_in_trick])
            self.winner = self.cards.index(trumpcards[best_trump])
        else:
            starting_index = self.leading_player_index
            first_card = self.cards[starting_index]
            played_suit = first_card[1]
            best_card = (max([i for (i, j) in self.cards if j == played_suit]), played_suit)
            self.winner = self.cards.index(best_card)

    def finished(self):
        if self.num_cards == 4:
            return True
        else:
            return False


class IllegalPlayerIndexException(Exception):
    pass
