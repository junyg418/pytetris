import sys
import pygame
from pygame.locals import *

from PageModuls.StartPage import *
from PageModuls.GameRunning import *

WHITE = (255,255,255)
GRAY = (66, 66, 66)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLO = (0, 255, 0)


FPS = 100
FramePerSec = pygame.time.Clock()
pygame.init()
size = (500,700)
GameDisplay = pygame.display.set_mode(size)
GameDisplay.fill(GRAY)
pygame.display.set_caption("tetris")

big_font = pygame.font.SysFont("malgungothicsemilight", 60)
middle_font = pygame.font.SysFont("malgungothicsemilight", 30)
little_font = pygame.font.SysFont("malgungothicsemilight", 16)

startPage(GameDisplay)

