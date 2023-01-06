class Ball:
    def __init__(self, name, catchRate=1) -> None:
        self.name = name
        self.catchRate = catchRate
class Potion:
    def __init__(self, name="Potion", healAmount=20) -> None:
        self.name = name
        self.healAmount = healAmount

class Bag:
    def __init__(self, balls: dict=dict(), poitons: dict=dict()) -> None:
        self.balls = balls
        self.potions = poitons

