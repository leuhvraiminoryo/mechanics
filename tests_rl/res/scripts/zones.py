class Map:
    def __init__(self,rooms=[],doors=[]):
        self.rooms = rooms
        self.doors = doors

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
    

