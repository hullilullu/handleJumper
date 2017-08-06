import pygame
import inputHandling
import gameLogic
import graphics

size = (700,500)
screen = pygame.display.set_mode(size)

pygame.init()
    
stageData = gameLogic.StageData()
inputData = {"grab": False, "run": True}

run = True
clock = pygame.time.Clock()

#-------- MAIN LOOP ----------
while run:
    #EVENTS
    inputData = inputHandling.handleInput(inputData)
    run = inputData["run"]

    if len(stageData.candy) <= 0:
        run = False
    elif stageData.mainCh.pos[0] < 0 or stageData.mainCh.pos[0] > size[0] or stageData.mainCh.pos[1]>size[1]:
        run = False
    #GAMELOGIC
    stageData.update(inputData)
    #DRAWING CODE
    screen.fill((0,0,0))
    graphics.draw(screen, stageData)
    pygame.display.flip()

    #set update speed 60 frame/s
    clock.tick(60)


pygame.quit()

    




