from res.scripts.utils import *

def play():
    player = Player()
    while True:
        SCR.fill(BLACK)
        checkForQuit()
        player.draw()
        player.move((random.randint(-5,5),random.randint(-5,5)))
        pygame.display.update()
        FPSCLOCK.tick(FPS) 