class Rank:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if self.value == 0:
            return "Seven"
        elif self.value == 1:
            return "Eight"
        elif self.value == 2:
            return "Nine"
        elif self.value == 3:
            return "Unter"
        elif self.value == 4:
            return "Ober"
        elif self.value == 5:
            return "King"
        elif self.value == 6:
            return "Ten"
        elif self.value == 7:
            return "Ace"

    def __hash__(self):
        return self.value

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def points(self):
        if self.value == 7:
            return 11
        elif self.value == 6:
            return 10
        elif self.value == 5:
            return 4
        elif self.value == 4:
            return 3
        elif self.value == 3:
            return 2
        else:
            return 0


SEVEN = Rank(0)
EIGHT = Rank(1)
NINE = Rank(2)
UNTER = Rank(3)
OBER = Rank(4)
KING = Rank(5)
TEN = Rank(6)
ACE = Rank(7)
ALL_RANKS = [SEVEN, EIGHT, NINE, TEN, UNTER, OBER, KING, ACE]
