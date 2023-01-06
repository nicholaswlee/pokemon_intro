import json
from statsClass import StatsStages

class MoveInfo:
    def __init__(self, category, basePower=0, physAtk=0, physDef=0, specialAtk=0, specialDef=0, spd=0, effect=None, status=None, chance=1) -> None:
        self.basePower = basePower
        self.category = category
        self.statMods = StatsStages(physAtk=physAtk, physDef=physDef, specialAtk=specialAtk, specialDef=specialDef, spd=spd)
        self.effect =effect
        self.status = status 
        self.chance = chance
    def __str__(self):
        txt = "{{basePower: {basePower}, statMods: {statMods}, effect: {effect}, status: {status}, chance: {chance}}}"
        return txt.format(basePower=self.basePower,statMods=self.statMods.__str__(), effect=self.effect.__str__(), status=self.status, chance=self.chance)
class Move:
    def __init__(self, name, type, category, accuracy, info: MoveInfo) -> None:
        self.name = name
        self.type = type
        self.category = category 
        self.accuracy = accuracy
        self.info = info
    def __str__(self):
        return self.name + ": " + self.type + ", " + self.category + ", " + str(self.accuracy) + ", " + self.info.__str__() 

def infoFromDict(jsonDict: dict):
    if(jsonDict == None):
        return None
    physAtk = 0
    physDef = 0
    spd = 0
    specialAtk = 0
    specialDef = 0
    chance = 1
    effect = None
    basePower = 0
    if("basePower" in jsonDict):
        basePower = jsonDict["basePower"]
    if("physAtk" in jsonDict):
        physAtk = jsonDict["physAtk"]
    if("specialAtk" in jsonDict):
        specialAtk = jsonDict["specialAtk"]
    if("specialDef" in jsonDict):
        specialDef = jsonDict["specialDef"]
    if("spd" in jsonDict):
        spd = jsonDict["spd"]
    if("physDef" in jsonDict):
        physDef = jsonDict["physDef"]
    if("chance" in jsonDict):
        chance = jsonDict["chance"]
    if("info" in jsonDict):
        effect = infoFromDict(jsonDict["info"])
    return MoveInfo(
        category=jsonDict["category"], 
        physAtk=physAtk,
        physDef= physDef,
        spd=spd,
        chance=chance,
        effect=effect,
        specialAtk=specialAtk,
        specialDef=specialDef,
        basePower=basePower)

def movefromDict(jsonDict: dict):
    return Move(jsonDict["name"], jsonDict["type"], jsonDict["category"], jsonDict["accuracy"], infoFromDict(jsonDict["info"]))
    
class MoveSet:
    def __init__(self) -> None:
        self.length = 0
        self.moves = []
    def __str__(self) -> str:
        string = ""
        for move in self.moves:
            string = string + move.__str__()
        return "length: " + str(self.length) + " Moves [" + string + "]"
    def addMove(self, move: Move):
        self.moves.append(move)
        self.length += 1 
        if(self.length > 4):
            self.moves.pop(0)
            self.length = self.length - 1
    def selectMove(self, index):
        return self.moves[index - 1]
    

def moveFromDict(jsonDict: dict):
    return Move(jsonDict["name"], jsonDict["type"], jsonDict["category"], jsonDict["accuracy"],info=moveFromDict(jsonDict["info"]))

def learnMoveSetFromLevels(moves, level) -> MoveSet:
    movesFile = open('moves.json')
    movesIndex = json.load(movesFile)
    moveSet = MoveSet()
    for move in moves:
        if move["level_learned"] <= level:
            moveSet.addMove(movefromDict(movesIndex[move["name"]]))
        else:
            break
    return moveSet





