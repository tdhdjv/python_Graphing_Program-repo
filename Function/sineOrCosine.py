from Function.function import Function
from coordinate import Coordinate
import math

class Sine(Function):
    def __init__(self, coordinate: Coordinate):
        super().__init__(coordinate)
    def func(self, x:float) :
        return math.sin(x)
class Cosine(Function):
    def __init__(self, coordinate: Coordinate):
        super().__init__(coordinate)
    def func(self, x:float) :
        return math.cos(x)