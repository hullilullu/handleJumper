import pygame

def handleInput(inputData):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inputData["run"] = False
        elif event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == 32:
                    inputData["grab"] = True
                if event.key == 113:
                    inputData["run"] = False
        elif event.type == pygame.KEYUP:
                print(event.key)
                if event.key == 32:
                    inputData["grab"] = False
    return inputData
    
    
