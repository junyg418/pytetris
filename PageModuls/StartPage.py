import pygame
import sys
from pygame import *
from PageModuls.GameRunning import *

WHITE = (255,255,255)

def startPage(GameDisplay):
    start_button = pygame.Rect((100, 440),(300, 130)) # 넓이: 100~ 400, 높이: 440~ 570
    pygame.draw.rect(GameDisplay, WHITE, start_button)

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

        # FramePerSec.tick(60)
        pygame.display.update()
    gameRunning(GameDisplay)
