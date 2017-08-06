import pygame

def handleInput(inputData):
    #inputData = {"grab": False, "run": True}


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inputData["run"] = False
        elif event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == 32:
                    inputData["grab"] = True
##                if event.key == pygame.K_DOWN:
##
##                if event.key == pygame.K_LEFT:
##
##                if event.key == pygame.K_RIGHT:
        elif event.type == pygame.KEYUP:
                print(event.key)
                if event.key == 32:
                    inputData["grab"] = False
    return inputData
    
    
