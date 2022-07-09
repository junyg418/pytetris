import pygame

BLACK = (0,0,0)

# middle_font = pygame.font.SysFont("malgungothicsemilight", 20)
bg = pygame.image.load('background.png')
def backgroundDraw(display):
    # pygame.draw.line(display, BLACK, (350,0), (350,700), 2)
    display.blit(bg,(0,0))