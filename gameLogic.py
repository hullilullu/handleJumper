import math
import gameObjects as go

#TEST

def getStageData():
    returnHash = {}
    returnHash["mainCh"] = go.MainCharacter([200, 100])
    returnHash["handles"] = [go.Handle(300,300,30), go.Handle(200,200, 40), go.Handle(200,300,20),
                        go.Handle(100,100,30), go.Handle(550,350, 10, 1, 0.14), go.Handle(40,180,20,2,0.15),
                        go.Handle(400,70,25,0.1,0.05), go.Handle(200,200, 40, 0, 0.07), go.Handle(350,250,10),
                        go.Handle(500,200,38,1,0.045),go.Handle(650,300,38,1,0.03),go.Handle(570,300,38,1,0.06),
                        go.Handle(430, 256, 19)]
    returnHash["candy"] = [go.Candy(0,[350, 50]),go.Candy(0,[200, 50]),go.Candy(0,[600, 150])]
    return returnHash

def updateStageData(inputData, stageData):
    if inputData["grab"] and not stageData["mainCh"].handle:
        for handle in stageData["handles"]:
            x = stageData["mainCh"].pos[0] - handle.getTipPos()[0]
            y = stageData["mainCh"].pos[1] - handle.getTipPos()[1]
            if x**2 + y**2 < 200:
                stageData["mainCh"].handle = handle
    elif not inputData["grab"]:
        stageData["mainCh"].handle = None
    stageData["mainCh"].update()
    for candy in stageData["candy"]:
        if (stageData["mainCh"].pos[0] - candy.pos[0])**2 + (stageData["mainCh"].pos[1] - candy.pos[1])**2 < 200:
            stageData["candy"].remove(candy)
    for handle in stageData["handles"]:
        handle.update()


