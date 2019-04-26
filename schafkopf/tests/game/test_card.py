import pytest

from schafkopf.schafkopf.game.cards import InvalidCardDefinitionException, Card


def test_invalid_card_definition():
    with pytest.raises(InvalidCardDefinitionException):
        Card(rank=1000, suit="e")
