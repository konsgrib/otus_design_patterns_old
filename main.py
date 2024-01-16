from math import sqrt
from typing import List

class Solver:
    @classmethod
    def solve(cls,a: float, b: float, c: float)-> List[float]:
        d = (b * b) - (4 * a * c)
        if  d < 0:
            return []
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)

        return [x1, x2]