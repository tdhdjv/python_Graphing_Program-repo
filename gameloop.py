
import pygame
import time
import sys
from game import Game


WINDOW_SIZE = (800, 800)

class Gameloop:

    def __init__(self):
        #make a game
        self._game = Game()

        pygame.init()
        print(pygame.version)

        #make window
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        self.display = pygame.Surface(WINDOW_SIZE)
        #set window setting
        pygame.display.set_caption("Graphing Program")

        self.loop()

    def loop(self):
        running = True

        previousTime = 0
        previousPrintTime = time.time()
        currentTime = time.time()
        updateAmount = 0

        while running:
            #elapsed time
            previousTime = currentTime
            currentTime = time.time()
            dt = currentTime - previousTime
            #update
            updateAmount += 1
            #render
            self.render()

            if previousPrintTime+1 < currentTime:
                print("The FPS is %d frames per sec" %updateAmount)
                previousPrintTime = currentTime
                updateAmount = 0

            #exit
            for event in pygame.event.get() :
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
    def render(self) :
        self.display.fill("white")
        
        self._game.render(self.display)

        self.window.blit(pygame.transform.scale(self.display, self.window.get_size()), (0, 0))
        pygame.display.update()