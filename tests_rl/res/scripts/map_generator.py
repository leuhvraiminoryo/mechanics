from res.scripts.zones import *
import os, random

correspondings_sides = {"u":"d","d":"u","r":"l","l":"r"}

def extractRooms():
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

rooms = extractRooms()

def createDoors(salle):
    '''Crée toutes les portes d'une salle, et les ajoutes à doors de la salle'''
    for i in range(1,len(salle.map)):
        for j in range(len(salle.map[1])):
            if salle.map[i][j] == 'd':
                salle.doors.append(Door((i,j)))

def generate_map():
    map = Map()
    map.rooms.append(Salle(random.choice(rooms['depart'])))
    print(map.rooms[0].map[0])
    createDoors(map.rooms[0])
    print(map.rooms[0].doors)
