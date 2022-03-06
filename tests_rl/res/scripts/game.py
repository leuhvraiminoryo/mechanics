from res.scripts.utils import *
from res.scripts.zones import *

def play():
    player = Player()
    map = Map(0,[Salle(['uld', '0000d0000', '000000000', '000000000', '000vvv000', 'd00vvv00d', '000vvv000', '000000000', '000000000', '0000d0000'])])
    while True:
        SCR.fill(BLACK)
        checkForQuit()
        map.drawCurrRoom()
        print(OnWhichTileTypeIsEntity(map.rooms[map.curr].map,player.pos))
        player.draw()
        player.move((random.randint(-5,5),random.randint(-5,5)))
        pygame.display.update()
        FPSCLOCK.tick(FPS) 
