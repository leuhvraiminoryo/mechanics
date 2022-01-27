#------------------- setup

import pygame, sys, random, math, time
from pygame.locals import *

pygame.mixer.init()

#init
global FPSCLOCK, SCR
pygame.init()
FPS = 60
FPSCLOCK = pygame.time.Clock()
WX = 800
WY = 500
C_X = 20
C_Y = 10
SCR = pygame.display.set_mode((WX, WY))
SCR.fill((255,25,36))
pygame.display.set_caption("yeet")
MUTE = False

#colors setup
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (155,155,155)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


#fonts setup
LARGEFONT = pygame.font.Font('freesansbold.ttf', 75)
BASICFONT = pygame.font.Font('freesansbold.ttf', 25)

#sound setup
pwop = pygame.mixer.Sound('res/sound/pwop.mp3')
intro_sound = pygame.mixer.Sound("res/sound/intro_sound.wav")

#image setup

logo = pygame.image.load('res/images/logo.png')

