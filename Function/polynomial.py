from coordinate import Coordinate
from Function.function import Function

class Polynomial(Function):
    def __init__(self, coordinate: Coordinate, coeffiecence:dict = {1: 1}):
        super().__init__(coordinate)
        self.coeffiecence = coeffiecence
    def func(self, x:float):
        result = 0
        for kvp in self.coeffiecence.items():
            result += kvp[1]*x**kvp[0]
        return result