from res.scripts.utils import *
from res.scripts.zones import *

def doorUse(door_id,map,player):
    for doors in map.doors:
        if doors.link == door_id:
            map.curr = doors.room
            player.pos = ConvertTilePosToEntityPos(map.rooms[map.curr].map,doors.pos)

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
    
    map.doors.append(Door((2,5),0,Door.id+1))
    map.doors.append(Door((7,3),1,Door.id-1))

    while True:
        SCR.fill(BLACK)
        checkForQuit()
        map.drawCurrRoom()
        tile = OnWhichTileTypeIsEntity(map.rooms[map.curr].map,player.pos)
        if tile == 'd':
            print('d')
            for doors in map.doors:
                if doors.room == map.curr and player.pos == ConvertTilePosToEntityPos(map.rooms[map.curr].map,doors.pos):
                    print('use')
                    doorUse(doors.id,map,player)
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
