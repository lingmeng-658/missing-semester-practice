def calculate_tax(price: float, rate: float) -> float:
    """Return the price after adding tax."""
    return price * (1 + rate)

def calculate_average(scores: list[int]) -> float:
    """Return the average of scores. Raise ValueError if list is empty."""
    if not scores:
        raise ValueError("scores list is empty")
    return sum(scores) / len(scores)


class Student:
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score

    def passed(self) -> bool:
        return self.score >= 60