from Function.function import Function
from coordinate import Coordinate
import math
import pygame

class Tangent(Function):
    def __init__(self, coordinate: Coordinate):
        super().__init__(coordinate)

    def func(self, x:float) :
        if x%math.pi == math.pi/2:
            return None
        return math.tan(x)
    
    def drawFunction(self, display, resolution = 10):
        from gameloop import WINDOW_SIZE
        points = []
        for screenX in range(0, WINDOW_SIZE[0] ,resolution):
            worldX = self.coordinate.screenToWorld((screenX,0))[0]
            worldY = self.func(worldX)
            if worldY == None or -resolution/self.coordinate.pixelPerUnit < (worldX+ math.pi/2)%math.pi < resolution/self.coordinate.pixelPerUnit:
                points.append((screenX, 0))
                if(len(points) >= 2): pygame.draw.lines(display, 'black', False, points)
                points.clear()
                points.append((screenX, WINDOW_SIZE[1]))
            else:
                points.append((screenX, self.coordinate.worldToScreen((0, worldY))[1]))
        if(len(points) >= 2): pygame.draw.lines(display, 'black', False, points)