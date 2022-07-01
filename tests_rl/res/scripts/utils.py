from tests_rl.res.scripts.config import *

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
    return [int(((x) - WX/2 + (l_x*(TILESIZE+GAP))/2)/(TILESIZE+GAP)),int(((y) - WY/2 + (l_y*(TILESIZE+GAP))/2)/(TILESIZE+GAP))]

def ConvertTilePosToEntityPos(room_map,tile_pos):
    l_x = len(room_map[1])
    l_y = len(room_map)

    x,y = tile_pos
    return [x*(TILESIZE+GAP) + WX/2 - (l_x*(TILESIZE+GAP))/2, y*(TILESIZE+GAP) + WY/2 - (l_y*(TILESIZE+GAP))/2]

def OnWhichTileTypeIsEntity(room_map,enti_coords):
    x,y = ConvertEntityPosToTilePos(room_map,enti_coords)
    if 1 <= y < len(room_map):
        if 0 <= x < len(room_map[y]):
            return room_map[y][x]


def verif_keys(pressed,left_click,right_click):
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                left_click = True
            if event.button == 3:
                right_click = True
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                left_click = False
            if event.button == 3:
                right_click = False
        pygame.event.post(event)
            


    for event in pygame.event.get(KEYUP):
        if event.key == K_UP:
            pressed["up"] = False
        if event.key == K_DOWN:
            pressed["down"] = False
        if event.key == K_RIGHT:
            pressed["right"] = False
        if event.key == K_LEFT:
            pressed["left"] = False
        if event.key == K_a:
            pressed["a"] = False
        if event.key == K_e:
            pressed["e"] = False
        if event.key == K_w:
            pressed["w"] = False
        if event.key == K_o:
            pressed["o"] = False
        if event.key == K_d:
            pressed["d"] = False
        if event.key == K_r:
            pressed["r"] = False
        if event.key == K_BACKSPACE:
            pressed["del"] = False
    
    for event in pygame.event.get(KEYDOWN):
        if event.key == K_UP:
            pressed["up"] = True
        if event.key == K_DOWN:
            pressed["down"] = True
        if event.key == K_RIGHT:
            pressed["right"] = True
        if event.key == K_LEFT:
            pressed["left"] = True
        if event.key == K_a:
            pressed["a"] = True
        if event.key == K_e:
            pressed["e"] = True
        if event.key == K_w:
            pressed["w"] = True
        if event.key == K_o:
            pressed["o"] = True
        if event.key == K_d:
            pressed["d"] = True
        if event.key == K_r:
            pressed["r"] = True
        if event.key == K_BACKSPACE:
            pressed["del"] = True

    return pressed, left_click, right_click


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
