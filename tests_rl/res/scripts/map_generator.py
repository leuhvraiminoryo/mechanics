from res.scripts.zones import *
import os, random

correspondings_sides = {"u":"d","d":"u","r":"l","l":"r"}

def extractTemplates():
    '''extrait toutes les templates présentes dans res.templates, et renvoie 
    un dictionaire de listes de listes contenant ces templates, et représentant 
    l'arborescence de racine res.templates'''
    
    rooms = {}

    directory = 'tests_rl/res/templates'

    for element in os.listdir(directory):
        e = os.path.join(directory, element)

        if os.path.isdir(e):
            liste = []
            for templ in os.listdir(e):
                room = []
                nut = os.path.join(e,templ)
                with open(nut) as file:
                    lines = file.readlines()
                    for line in lines:
                        room.append(line.replace('\n',''))
                liste.append(room)
            rooms[element] = liste

        if os.path.isfile(e):
            room = []
            with open(e) as file:
                lines = file.readlines()
                for line in lines:
                    room.append(line.replace('\n',''))
            rooms[element] = room

    return rooms



# here starts an ultimate spaghetty nightmare - good luck to whomever may be reading this

rooms = extractTemplates()
print(rooms['depart'][0])

def createOtherDoors(salle):
    coordOfExistingDoors = []
    for door in salle.doors:
        coordOfExistingDoors.append(door.pos)
    '''Crée toutes les portes d'une salle, et les ajoutes à doors de la salle'''
    for i in range(1,len(salle.map)):
        for j in range(len(salle.map[1])):
            if salle.map[i][j] == 'd' and not (i,j) in coordOfExistingDoors:
                salle.doors.append(Door((i,j)))

def addLinkDoor(map,salle,outer_door,cor):
     for i in range(1,len(salle.map)):
        for j in range(len(salle.map[1])):
            if salle.map[i][j] == 'd':
                if i == len(salle.map) and cor == 'd':
                    map.doors.append(Door((i,j),room=salle.id,porte_linked=[outer_door.id]))
                    outer_door.porte_linked.append(salle.doors[-1].id)

def link_rooms(map,room):

    if len(map.rooms) > 7:
        return

    createOtherDoors(room)

    for door in room.doors:

        if door.pos[0] <= 1:
            cor = 'd'
        if door.pos[0] >= len(room.map[1]):
            cor = 'u'
        if door.pos[0] < len(room.map):
            cor = 'r'
        if door.pos[0] >= len(room.map)/2:
            cor = 'l'

        map.rooms.append(Salle(random.choice(rooms[random.choice(ROOMTYPES)])))

        while cor not in map.rooms[-1].map[0]:
            map.rooms.pop()
            map.rooms.append(Salle(random.choice(rooms[random.choice(ROOMTYPES)])))
        
        addLinkDoor(map,map.rooms[-1],door,cor)

        link_rooms(map,map.rooms[-1])

def generate_map():
    '''génère une map composée du plusieurs salles et de leurs portes associées.
    utilise pour cela les classes Map, Salle, et Door de zones.py'''

    map = Map()
    map.rooms.append(Salle(random.choice(rooms['depart'])))
    link_rooms(map,map.rooms[0])
    return map

