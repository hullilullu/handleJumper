import math

class StageData:
    def __init__(self):
        self.mainCh = MainCharacter([200, 100])
        self.handles = [Handle(300,300,30), Handle(200,200, 40), Handle(200,300,20),
                        Handle(100,100,30), Handle(550,350, 10, 1, 0.14), Handle(40,180,20,2,0.15),
                        Handle(400,70,25,0.1,0.05), Handle(200,200, 40, 0, 0.07), Handle(350,250,10),
                        Handle(500,200,38,1,0.045),Handle(650,300,38,1,0.03),Handle(570,300,38,1,0.06),
                        Handle(430, 256, 19)]
        self.candy = [Candy(0,[350, 50]),Candy(0,[200, 50]),Candy(0,[600, 150])]
    def update(self, inputData):
        if inputData["grab"] and not self.mainCh.handle:
            for handle in self.handles:
                x = self.mainCh.pos[0] - handle.getTipPos()[0]
                y = self.mainCh.pos[1] - handle.getTipPos()[1]
                if x**2 + y**2 < 200:
                    self.mainCh.handle = handle
        elif not inputData["grab"]:
            self.mainCh.handle = None
        self.mainCh.update()
        for candy in self.candy:
            if (self.mainCh.pos[0] - candy.pos[0])**2 + (self.mainCh.pos[1] - candy.pos[1])**2 < 200:
                self.candy.remove(candy)
        for handle in self.handles:
            handle.update()
                
            
        



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
        
