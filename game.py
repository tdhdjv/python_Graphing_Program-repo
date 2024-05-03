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
        self._functions.append(Tangent(self.coordinate))
        self._functions.append(LogFunc(self.coordinate))
    def render(self, display: SurfaceType):
        self.coordinate.renderCoordinate(display)
        for function in self._functions:
            function.drawFunction(display)
    def update(self, dt:float):
        self.coordinate.update(dt)