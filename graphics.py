import pygame

def draw(screen, obj):
    for handle in obj.handles:
        pygame.draw.line(screen, (200,200,200),
                         (handle.x, handle.y),
                         (handle.getTipPos()),
                         4)
    for candy in obj.candy:
        pygame.draw.circle(screen, (255, 0, 10), candy.pos, 10)
    pygame.draw.circle(screen, (100, 245, 100), obj.mainCh.getIntPos(), 5)
    
