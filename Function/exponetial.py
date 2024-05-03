from Function.function import Function
from coordinate import Coordinate
import math

class Exponential(Function):
    def __init__(self, coordinate: Coordinate , base = math.e):
        super().__init__(coordinate)
        self.base = base
    def func(self, x:float) :
        return math.pow(self.base, x)