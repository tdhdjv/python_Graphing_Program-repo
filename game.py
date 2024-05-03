import pygame
from pygame import SurfaceType
from coordinate import Coordinate
from Function.testFunction import TestFunction
from Function.polynomial import Polynomial
from Function.exponetial import Exponential
from Function.logFunc import LogFunc
from Function.sineOrCosine import Sine, Cosine
from Function.tangent import Tangent
import time


class Game:
    def __init__(self):
        self.coordinate = Coordinate()
        self._functions = []
        self._functions.append(TestFunction(self.coordinate))
        self._functions.append(Polynomial(self.coordinate, {3: 2, 2:-3, 1:0, 0: 1}))
        self._functions.append(Exponential(self.coordinate, 0.5))
        self._functions.append(LogFunc(self.coordinate))
        self._functions.append(Sine(self.coordinate))
        self._functions.append(Cosine(self.coordinate))
        self._functions.append(Tangent(self.coordinate))
    def render(self, display: SurfaceType):
        self.coordinate.renderCoordinate(display)
        for function in self._functions:
            function.drawFunction(display)
    def update(self, dt:float):
        pass