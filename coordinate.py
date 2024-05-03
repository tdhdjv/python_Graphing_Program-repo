import pygame

class Coordinate:
    def __init__(self):
        self.originWorldPos = (130, 500)
        self.pixelPerUnit = 100
    
    def worldToScreen(self, point:tuple):
        x, y = point[0],  point[1]
        pixelPerUnit, originWorldPos = self.pixelPerUnit, self.originWorldPos
        return (x*pixelPerUnit+originWorldPos[0],-y*pixelPerUnit+originWorldPos[1])
    def screenToWorld(self, point:tuple):
        x, y= point[0],  point[1]
        pixelPerUnit, originWorldPos = self.pixelPerUnit, self.originWorldPos
        return ((x-originWorldPos[0])/pixelPerUnit,-(y-originWorldPos[1])/self.pixelPerUnit)

    def renderCoordinate(self, display):
        from gameloop import WINDOW_SIZE
        color = color = (200,200,200)
        x = self.originWorldPos[0] % self.pixelPerUnit
        while x < WINDOW_SIZE[0]:
            if x == self.originWorldPos[0]:
                color = (100,100,100)
            else:
                color = (200,200,200)
            pygame.draw.line(display, color, (x, 0), (x, WINDOW_SIZE[1]))
            x+=self.pixelPerUnit
        
        y = self.originWorldPos[1] % self.pixelPerUnit
        while y < WINDOW_SIZE[1]:
            if y == self.originWorldPos[1]:
                color = (100,100,100)
            else:
                color = color = (200,200,200)
            pygame.draw.line(display, color, (0, y), (WINDOW_SIZE[0], y))
            y+=self.pixelPerUnit