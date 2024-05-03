import pygame
from coordinate import Coordinate
from abc import ABC, abstractmethod


class Function(ABC):

    def __init__(self, coordinate: Coordinate):
        
        self.coordinate = coordinate
    @abstractmethod
    def func(self, x:float):
        pass

    def drawFunction(self, display, resolution = 10):
        from gameloop import WINDOW_SIZE
        points = []
        for screenX in range(0, WINDOW_SIZE[0] ,resolution):
            worldX = self.coordinate.screenToWorld((screenX,0))[0]
            worldY = self.func(worldX)
            if worldY == None:
                if(len(points) >= 2): pygame.draw.lines(display, 'black', False, points)
                points.clear()
            else:
                points.append((screenX, self.coordinate.worldToScreen((0, worldY))[1]))
        pygame.draw.lines(display, 'black', False, points)