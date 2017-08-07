import math

class MainCharacter:
    def __init__(self, pos):
        self.pos = pos
        self.velocity = [0,0]
        self.handle = None
        self.gravAcc = 0.02
    def update(self):
        if self.handle:
            self.pos = self.handle.getTipPos()
            self.velocity = self.handle.getTipVelocity()
        else:
            self.pos[0] += self.velocity[0]
            self.velocity[1] += self.gravAcc
            self.pos[1] += self.velocity[1]
    def getIntPos(self):
        return (int(self.pos[0]),int(self.pos[1]))
            

class Candy:
    def __init__(self, kind, pos):
        self.pos = pos
        self.kind = kind

class Handle:
    def __init__(self, x, y, length, angle = 0, speed = 0.1):
        self.x = x
        self.y = y
        self.length = length
        self.speed = speed
        self.angle = angle
    def update(self):
        self.angle += self.speed
        
    def getTipPos(self):
        return [self.x+(self.length*math.cos(self.angle)), (self.y+(self.length*math.sin(self.angle)))]
    def getTipVelocity(self):
        return [-self.speed*self.length*math.sin(self.angle), (self.speed*self.length*math.cos(self.angle))]
        
