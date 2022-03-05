from res.scripts.config import *

#-------------------- utils defs
def terminate(reason):
    '''Quitte'''
    pygame.quit()
    sys.exit(reason)

def checkForQuit():
    '''Vérifie s'il faut quitter'''
    for event in pygame.event.get(QUIT):
        terminate("WINDOW CLOSED")
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate("WINDOW CLOSED")
        pygame.event.post(event)


def makeText(font,text, color, bgcolor, x, y):

    textSurf = font.render(text, True, color, bgcolor)

    textRect = textSurf.get_rect()

    textRect.center = (x, y)

    return textSurf, textRect


def showText(font,text,color,bgcolor,x,y):
    textSurf,textRect = makeText(font,text,color,bgcolor,x,y)
    SCR.blit(textSurf,textRect)

def playSound(music):
    if not MUTE:
        pygame.mixer.Sound.play(music)
    return


class Player:
    def __init__(self,pos=[WX/2,WY/2],color=WHITE,size=15):
        self.pos = pos
        self.color = color
        self.size = size

    def move(self,vec):

        self.pos[0] += vec[0]
        if self.pos[0] < 0:
            self.pos[0] = 0
        if self.pos[0] > WX:
            self.pos[0] = WX

        self.pos[1] += vec[1]
        if self.pos[1] < 0:
            self.pos[1] = 0
        if self.pos[1] > WY:
            self.pos[1] = WY

    def draw(self):
        pygame.draw.circle(SCR,self.color,self.pos,self.size)