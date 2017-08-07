import pygame

def draw(screen, stageData):
    for handle in stageData["handles"]:
        pygame.draw.line(screen, (200,200,200),
                         (handle.x, handle.y),
                         (handle.getTipPos()),
                         4)
    for candy in stageData["candy"]:
        pygame.draw.circle(screen, (255, 0, 10), candy.pos, 10)
    pygame.draw.circle(screen, (100, 245, 100), stageData["mainCh"].getIntPos(), 5)
    
