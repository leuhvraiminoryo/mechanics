from res.scripts.config import *

#-------------------- utils defs
def terminate(reason):
    '''Quitte'''
    pygame.quit()
    sys.exit(reason)

def checkForQuit():
    '''Vérifie s'il faut quitter'''
    for event in pygame.event.get(QUIT):
        terminate("WINDOW CLOSED")
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate("WINDOW CLOSED")
        pygame.event.post(event)


def makeText(font,text, color, bgcolor, x, y):

    textSurf = font.render(text, True, color, bgcolor)

    textRect = textSurf.get_rect()

    textRect.center = (x, y)

    return textSurf, textRect


def showText(font,text,color,bgcolor,x,y):
    textSurf,textRect = makeText(font,text,color,bgcolor,x,y)
    SCR.blit(textSurf,textRect)


def showOpeningCutscene():
    start = time.time()
    playSound(intro_sound)
    passed = 0
    alph = 0

    while passed < 6:
        passed = time.time() - start
        SCR.fill(BLACK)

        showText(BASICFONT,"Made By Minoryo",WHITE,BLACK,WX/2,WY/2-90)
        if passed >= 2.5:
            alph += passed
            logo.set_alpha(alph)
            SCR.blit(logo,(WX/2-64,WY/2-64))
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def playSound(music):
    if not MUTE:
        pygame.mixer.Sound.play(music)
    return