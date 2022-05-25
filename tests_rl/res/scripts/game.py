from res.scripts.utils import *
from res.scripts.zones import *
from res.scripts.map_generator import *

def doorUse(door_id,map,player):
    map.door_use_cooldown = time.time()
    for doors in map.doors:
        if doors.link == door_id:
            map.curr[0] = doors.room
            #print(doors.room)
            player.pos = ConvertTilePosToEntityPos(map.rooms[map.curr[0]].map,[doors.pos_in_room[1],doors.pos_in_room[0]])
            return 
            
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
    '''map = Map(0,[Salle(['uld', 'vvvvvvvvvvv','v0000d0000v', 'v00c000000v', 'v000000000v', 'v000vvv000v', 'vd00vvv00dv', 'v000vvv000v', 'v000000000v', 'v000000000v', 'v0000d0000v','vvvvvvvvvvv']),Salle(['vvvvvvv','v00d00v','v00000v','v00000v','v00000v','v00000v','v00000v','v00d00v','vvvvvvv']),Salle(['lrd', '000000000000000000000000', '000000000000000000000000', '000000000000000000000000', '000000000000000000000000', '000000000000000000000000', '000000000000000000000000', '000000000000000000000000', '000000000000000000000000', '000000000000000000000000', 'd0000000000000000000000d', '000000000000000000000000', '000000000000000000000000', '000000000000000000000000', '000000000000000000000000', '000000000000000000000000', '000000000000000000000000', '000000000000000000000000', '000000000000000000000000', '00000000000d000000000000'])])
    
    print(ConvertEntityPosToTilePos(map.rooms[map.curr[0]].map,ConvertTilePosToEntityPos(map.rooms[map.curr[0]].map,(6,6))))
    
    map.doors.append(Door((2,5),0,1))
    map.doors.append(Door((7,3),1,0))'''

    map = generate_map()
    for door in map.doors:
        print(door.id,door.link)
    for room in map.rooms:
        print(room.id)

    while True:
        SCR.fill(BLACK)
        checkForQuit()
        map.drawCurrRoom()
        tile = OnWhichTileTypeIsEntity(map.rooms[map.curr[0]].map,player.pos)
        if tile == 'd':
            x,y = ConvertEntityPosToTilePos(map.rooms[map.curr[0]].map,player.pos)
            for doors in map.doors:
                if doors.room == map.curr[0] and [y,x] == list(doors.pos_in_room) and time.time() - map.door_use_cooldown > 5:
                    print("dooruse")
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
        player.move(vec,map.rooms[map.curr[0]].map)
        pygame.display.update()
        FPSCLOCK.tick(FPS) 
