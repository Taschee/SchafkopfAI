class Suit:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if self.value == 0:
            return "No suit"
        elif self.value == 1:
            return "Bells"
        elif self.value == 2:
            return "Hearts"
        elif self.value == 3:
            return "Leaves"
        elif self.value == 4:
            return "Acorns"

    def __eq__(self, other):
        if type(other) is type(self):
            return self.value == other.value
        return False

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return not self > other


NO_SUIT = Suit(0)
BELLS = Suit(1)
HEARTS = Suit(2)
LEAVES = Suit(3)
ACORNS = Suit(4)
ALL_SUITS = [BELLS, HEARTS, LEAVES, ACORNS]
SUITS_WITHOUT_HEARTS = [BELLS, LEAVES, ACORNS]
