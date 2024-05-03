import pygame
from coordinate import Coordinate
from abc import ABC, abstractmethod


class Function(ABC):

    def __init__(self, coordinate: Coordinate):
        
        self.coordinate = coordinate
    @abstractmethod
    def func(self, x:float):
        pass
    def derivative(self, x:float, dx: float = 0.01):
        return (self.func(x+dx)-self.func(x))/dx
    
    def acceleration(self, x:float, dx: float = 0.5):
        return (self.derivative(x+dx)-self.derivative(x))/dx

    def drawFunction(self, display, resolution = 10):
        from gameloop import WINDOW_SIZE
        points = []
        screenX = 0
        while screenX <= WINDOW_SIZE[0]:
            worldX = self.coordinate.screenToWorld((screenX,0))[0]
            worldY = self.func(worldX)
            if worldY == None:
                if(len(points) >= 2): pygame.draw.lines(display, 'black', False, points)
                points.clear()
            else:
                points.append((screenX, self.coordinate.worldToScreen((0, worldY))[1]))
            screenX += min(resolution, max(1,WINDOW_SIZE[0]-screenX))
        if(len(points) >= 2):pygame.draw.lines(display, 'black', False, points)