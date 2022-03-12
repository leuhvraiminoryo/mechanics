from res.scripts.utils import *
from res.scripts.zones import *

def doorUse(door,map):
    for room in map.rooms:
        for doors in room.doors:
            if doors == door.link:
                map.curr_id = map.rooms.index(room)

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
    map = Map(0,[Salle(['uld', 'vvvvvvvvvvv','v0000d0000v', 'v00c000000v', 'v000000000v', 'v000vvv000v', 'vd00vvv00dv', 'v000vvv000v', 'v000000000v', 'v000000000v', 'v0000d0000v','vvvvvvvvvvv']),Salle(['vvvvvvv','v00d00v','v00000v','v00000v','v00000v','v00000v','v00000v','v00d00v','vvvvvvv'])])
    
    print(ConvertEntityPosToTilePos(map.rooms[map.curr].map,ConvertTilePosToEntityPos(map.rooms[map.curr].map,(6,6))))
    
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
