import pygame
from pygame.locals import * # type: ignore
import sys

# initialize pygame
pygame.init()

# limiting frames
FPS = 60
FramePerSec = pygame.time.Clock()

# predefined colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# set up display
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")