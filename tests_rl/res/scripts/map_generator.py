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

def createOtherDoors(salle,door_to_link=None,pos_to_link=None):
    coordOfExistingDoors = []
    for door in salle.doors:
        coordOfExistingDoors.append(door.pos)
    '''Crée toutes les portes d'une salle, et les ajoutes à doors de la salle'''
    for i in range(1,len(salle.map)):
        for j in range(len(salle.map[1])):
            if salle.map[i][j] == 'd' and not (i,j) in coordOfExistingDoors:
                salle.doors.append(Door((i,j)))

def link_rooms(map,room):
    createOtherDoors(room)
    for door in room.doors:

        if door.pos[0] == 1:
            dir = 'u'
        if door.pos[0] == len(room.map[1]):
            dir = 'd'
        if door.pos[0] == 0:
            dir = 'l'
        if door.pos[0] == len(room.map):
            dir = 'r'

        map.rooms.append(Salle(random.choice(rooms[random.choice(ROOMTYPES)])))
        while dir not in map.rooms[-1][0]:
            map.rooms.pop()
            map.rooms.append(Salle(random.choice(rooms[random.choice(ROOMTYPES)])))
        
        createOtherDoors(map.rooms[-1],door,dir)

def generate_map():
    '''génère une map composée du plusieurs salles et de leurs portes associées.
    utilise pour cela les classes Map, Salle, et Door de zones.py'''

    map = Map()
    map.rooms.append(Salle(random.choice(rooms['depart'])))
    link_rooms(map,map.rooms[0])

