from res.scripts.utils import *
from res.scripts.zones import *

def play():
    left_click = False
    right_click = False


    pressed = {
        "up" : False,
        "down" : False,
        "right" : False,
        "left" : False,
        "a" : False,
        "r" : False,
        "o" : False,
        "d" : False,
        "e" : False,
        "w" : False,
        "del" : False
    }


    player = Player()
    map = Map(0,[Salle(['uld', '0000d0000', '00c000000', '000000000', '000vvv000', 'd00vvv00d', '000vvv000', '000000000', '000000000', '0000d0000'])])
    while True:
        SCR.fill(BLACK)
        checkForQuit()
        map.drawCurrRoom()
        print(OnWhichTileTypeIsEntity(map.rooms[map.curr].map,player.pos))
        player.draw()
        pressed,left_click,right_click = verif_keys(pressed,left_click,right_click)
        vec = [0,0]
        if pressed['left']:
            vec[0] -= 5
        if pressed['right']:
            vec[0] += 5
        if pressed['up']:
            vec[1] -= 5
        if pressed['down']:
            vec[1] += 5
        player.move(vec,map.rooms[map.curr].map)
        pygame.display.update()
        FPSCLOCK.tick(FPS) 
