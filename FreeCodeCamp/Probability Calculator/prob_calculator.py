import copy
import random

# Consider using the modules imported above.
from typing import Dict, List


class Hat:
    def __init__(self, **named_values) -> None:
        self.balls = []
        for k, v in named_values.items():
            for _ in range(v):
                self.balls.append(k)

    def draw(self, amount: int) -> List:
        drawn = []
        if amount >= len(self.balls):
            return self.balls
        else:
            for _ in range(amount):
                choice = random.randrange(len(self.balls))
                drawn.append(self.balls.pop(choice))
        return drawn


def experiment(hat: Hat, expected_balls: Dict, num_balls_drawn: int, num_experiments: int):
    count = 0
    for _ in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        drawn_balls = copy_hat.draw(num_balls_drawn)
        passed = True
        for k, v in expected_balls.items():
            if drawn_balls.count(k) < v:
                passed = False
                break
        if passed:
            count += 1
    return count / num_experiments
