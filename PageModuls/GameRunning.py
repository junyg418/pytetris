import pygame
from pygame import *
import sys

from Graphic import backgroundDraw


def gameRunning(GameDisplay):
    # GameDistplay.fill(WHITE)
    game_run = True
    tetris_arr = []
    while game_run:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        backgroundDraw(GameDisplay)

        # game_run = False
        pygame.display.update()
    gameOver()
    
def gameOver():
    pass
    
