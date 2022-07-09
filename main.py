import sys
import pygame
from pygame.locals import *

from Graphic import backgroundDraw


WHITE = (255,255,255)
GRAY = (66, 66, 66)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLO = (0, 255, 0)


FPS = 100
FramePerSec = pygame.time.Clock()
pygame.init()
size = (500,700)
GameDistplay = pygame.display.set_mode(size)
GameDistplay.fill(GRAY)
pygame.display.set_caption("tetris")

big_font = pygame.font.SysFont("malgungothicsemilight", 60)
middle_font = pygame.font.SysFont("malgungothicsemilight", 30)
little_font = pygame.font.SysFont("malgungothicsemilight", 16)

def startPage():
    start_button = pygame.Rect((100, 440),(300, 130)) # 넓이: 100~ 400, 높이: 440~ 570
    pygame.draw.rect(GameDistplay, WHITE, start_button)
    start = True
    while start:
        mouse = pygame.mouse.get_pos()
        button_hobber = 100 <= mouse[0] <= 400 and 440 <= mouse[1] <= 570 # 마우스가 버튼 위에 있을 때 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONUP:
                if button_hobber:  # 버튼 클릭 했을 때
                    start = False

        if button_hobber: # 마우스가 버튼 위에 있을 때
            if start_button.width <= 305:
                start_button.update(start_button.x+1, start_button.y+1, start_button.width+1, start_button.height+1)
        else:
            if start_button.width != 300:
                start_button.update(start_button.x-1, start_button.y-1, start_button.width-1, start_button.height-1)

        FramePerSec.tick(FPS)
        pygame.display.update()
    gameRunning()



def gameRunning():
    # GameDistplay.fill(WHITE)
    game_run = True
    tetris_arr = []
    while game_run:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        backgroundDraw(GameDistplay)

        # game_run = False
        pygame.display.update()
    gameOver()
    
def gameOver():
    pass
    
startPage()