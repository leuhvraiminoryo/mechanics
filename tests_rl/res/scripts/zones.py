class Salle:
    id = 0
    def __init__(self, map):
        self.id = id 
        self.map = map
        self.link = {}
        Salle.id += 1

    def link(self,id):
        pass

class Door:
    id = 0
    def __init__(self, pos, porte_linked):
        self.pos = pos
        self.link = porte_linked
        Door.id += 1
    

