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

def ConvertEntityPosToTilePos(room_map,enti_coords):
    l_x = len(room_map[1])
    l_y = len(room_map)

    x,y = enti_coords
    return [round(((x) - WX/2 + (l_x*(TILESIZE+GAP))/2)/(TILESIZE+GAP)),round(((y) - WY/2 + (l_y*(TILESIZE+GAP))/2)/(TILESIZE+GAP))]

def OnWhichTileTypeIsEntity(room_map,enti_coords):
    x,y = ConvertEntityPosToTilePos(room_map,enti_coords)
    if 0 <= y < len(room_map):
        if 0 <= x < len(room_map[y]):
            return room_map[y][x]
class Player:
    def __init__(self,pos=[WX/2.5,WY/2.5],color=WHITE,size=7):
        self.lastpos = pos
        self.pos = pos
        self.color = color
        self.size = size

    def move(self,vec,roommap):
        self.lastpos = list(self.pos)

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
        
        if OnWhichTileTypeIsEntity(roommap,self.pos) in [None,"v"]:
            self.pos = list(self.lastpos)

    def draw(self):
        pygame.draw.circle(SCR,self.color,self.pos,self.size)
