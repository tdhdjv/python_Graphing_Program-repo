from Function.function import Function
from coordinate import Coordinate
import math
import pygame

class LogFunc(Function):
    def __init__(self, coordinate: Coordinate , base = math.e):
        super().__init__(coordinate)
        self.base = base

    def func(self, x:float) :
        if x <= 0 or self.base == 1 or self.base < 0: return
        return math.log(x, self.base)
    
    def drawFunction(self, display, resolution = 10):
        from gameloop import WINDOW_SIZE
        points = []
        for screenY in range(0, WINDOW_SIZE[1] ,resolution):
            worldY = self.coordinate.screenToWorld((0, screenY))[1]
            worldX = math.pow(self.base, worldY)
            if worldX == None:
                if(len(points) >= 2): pygame.draw.lines(display, 'black', False, points)
                points.clear()
            else:
                points.append((self.coordinate.worldToScreen((worldX+1, 0))[0], screenY))
        pygame.draw.lines(display, 'black', False, points)