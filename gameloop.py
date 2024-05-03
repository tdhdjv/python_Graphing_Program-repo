import pygame
import time
import sys

class Gameloop:

    WINDOW_SIZE = (800, 800)
    def __init__(self):
        pygame.init()
        print(pygame.version)

        #make window
        self.window = pygame.display.set_mode(Gameloop.WINDOW_SIZE)
        self.display = pygame.Surface(Gameloop.WINDOW_SIZE)
        #set window setting
        pygame.display.set_caption("Graphing Program")

        self.loop()
    def loop(self):
        running = True

        previousTime = 0
        currentTime = time.time()
        
        while running:
            #elapsed time
            previousTime = currentTime
            currentTime = time.time()
            dt = currentTime - previousTime

            #update
            
            #render

            #exit
            for event in pygame.event.get() :
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()