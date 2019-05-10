
class GameType:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if self.value == 0:
            return "No game"
        elif self.value == 1:
            return "Partner mode"
        elif self.value == 2:
            return "Wenz"
        elif self.value == 3:
            return "Solo"

    def __gt__(self, other):
        assert type(other) == GameType, "Cannot compare game type with different object"
        return self.value > other.value

    def __lt__(self, other):
        assert type(other) == GameType, "Cannot compare game type with different object"
        return self.value < other.value



NO_GAME = GameType(0)
PARTNER_MODE = GameType(1)
WENZ = GameType(2)
SOLO = GameType(3)
GAME_MODES = [NO_GAME, PARTNER_MODE, WENZ, SOLO]