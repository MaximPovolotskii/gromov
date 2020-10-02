import pygame
from pygame.draw import *

pygame.init()

FPS = 10
screen = pygame.display.set_mode((400, 400))

def face(x):
    """
    draws a face
    x adjusts red component of the face colour
    also x adjusts the eyebrows and the mouth
    """
    rect(screen, (169, 176, 184), (0, 0, 400, 400), 0)
    circle(screen, (255, 255 - 5 * x, 51 - x), (200, 200), 150)
    line(screen, (0, 0, 0), (70, 60), (180, 150 - 51 + x), 20)
    circle (screen, (255, 0, 0), (150, 165), 25)
    circle (screen, (0, 0, 0), (150, 165), 10)
    line(screen, (0, 0, 0), (220, 150 - 51 + x), (330, 90), 20)
    circle (screen, (255, 0, 0), (250, 165), 20)
    circle (screen, (0, 0, 0), (250, 165), 10)
    rect(screen, (0, 0, 0), (120, 260, 160, 30 - int(x / 2)), 0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

k = 0
while not finished:
    clock.tick(FPS)
    face(k)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    if k < 51:
        k += 1
    else:
        k = 0
    pygame.display.flip()

pygame.quit()
