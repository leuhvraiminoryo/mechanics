import os

correspondings_sides = {"u":"d","d":"u","r":"l","l":"r"}

def extractRooms():
    rooms = []

    directory = 'tests_rl/res/templates'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            room = []
            with open(f) as file:
                lines = file.readlines()
                for line in lines:
                    room.append(line.replace('\n',''))
            rooms.append(room)
    return rooms

rooms = extractRooms()
for i in rooms:
    print(i)