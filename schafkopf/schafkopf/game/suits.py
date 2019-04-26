
class Suit:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if self.value == 0:
            return "Bells"
        elif self.value == 1:
            return "Hearts"
        elif self.value == 2:
            return "Leaves"
        elif self.value == 3:
            return "Acorns"

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value


BELLS = Suit(0)
HEARTS = Suit(1)
LEAVES = Suit(2)
ACORNS = Suit(3)
ALL_SUITS = [BELLS, HEARTS, LEAVES, ACORNS]
SUITS_WITHOUT_HEARTS = [BELLS, LEAVES, ACORNS]
