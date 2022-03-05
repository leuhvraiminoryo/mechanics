from res.scripts.config import *
class Map:
    def __init__(self,curr_room_id_in_rooms_list=0,rooms=[]):
        self.curr = curr_room_id_in_rooms_list
        self.rooms = rooms #list of all doors in Da Map
    
    def drawCurrRoom(self):
        tile_color = {"0":WHITE,"d":BLUE}
        curr_room = self.rooms[self.curr]
        l_x = len(curr_room.map[1])
        l_y = len(curr_room.map)

        for y in range(0, l_x):
            for x in range(1, l_y):
                rect = pygame.Rect(x*TILESIZE + WX/2 - (l_x*TILESIZE)/2, y*TILESIZE + WY/2 - (l_y*TILESIZE)/2, TILESIZE, TILESIZE)
                pygame.draw.rect(SCR, tile_color[curr_room.map[x][y]], rect, 1)


class Salle:
    id = 0
    def __init__(self, map, doors=[]):
        self.id = Salle.id 
        self.map = map
        self.doors = doors #list of all ids of doors in Da Room
        Salle.id += 1

    def link(self,id):
        self.link.append(id)

class Door:
    id = 0
    def __init__(self, pos, porte_linked=None):
        self.id = Door.id
        self.pos = pos
        self.link = porte_linked #Da Related Door's id
        Door.id += 1
    

