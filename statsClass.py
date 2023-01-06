import math
modifications = {
    -6 : 0.25,
    -5 : 0.2825,
    -4 : 0.33,
    -3 : 0.4,
    -2 : 0.5,
    -1 : 0.66,
     0 : 1,
     1 : 1.5,
     2 : 2,
     3 : 2.5,
     4 : 3,
     5 : 3.5,
     6 : 4
}

class StatsStages():
    def __init__(self, hp=0, physAtk=0, physDef=0, specialAtk=0, specialDef=0, spd=0) -> None:
        self.physAtk = physAtk
        self.physDef = physDef
        self.specialAtk = specialAtk
        self.specialDef = specialDef
        self.spd = spd
    def __str__(self):
        txt = "{{physAtk: {physAtk}, physDef: {physDef}, specialAtk: {specialAtk}, specialDef: {specialDef}" + ", spd: {spd}}}"
        return txt.format(physAtk=self.physAtk, physDef=self.physDef, specialAtk=self.specialAtk,
                            specialDef=self.specialDef, spd=self.spd,)
    def applyStatMods(self, mods, name):
        response = ""
        response = response + createPhrase(name, "attack", mods.physAtk)
        self.physAtk = self.physAtk + mods.physAtk
        response = response + createPhrase(name, "defense", mods.physDef)
        self.physDef = self.physDef + mods.physDef
        response = response + createPhrase(name, "special attack", mods.specialAtk)
        self.specialAtk = self.specialAtk + mods.specialAtk
        response = response + createPhrase(name, "special defense", mods.specialDef)
        self.specialDef = self.specialDef + mods.specialDef
        response = response + createPhrase(name, "speed", mods.spd)
        self.spd = self.spd + mods.spd
        return response
        

    
class Stats():
    def __init__(self, hp: int, physAtk: int, physDef: int, specialAtk: int, specialDef: int, spd: int) -> None:
        self.hp = hp
        self.physAtk = physAtk
        self.physDef = physDef
        self.specialAtk = specialAtk
        self.specialDef = specialDef
        self.spd = spd

def createPhrase(name, stat, value):
    response = ""
    if(value == 1):
            response = name + "'s " + stat + " rose. "
    elif(value== 2):
        response = name + "'s " + stat + " sharply rose. "
    elif(value== -1):
        response = name + "'s " + stat + " fell. "
    elif(value== -2):
        response = name + "'s " + stat + " sharply fell. "
    return response
    
def calculateBattleStats(baseStats: Stats, mods: StatsStages, hp=-1) -> Stats:
    hitPoints = hp
    if(hp == -1):
        hitPoints = baseStats.hp
    return Stats(
        hitPoints,
        baseStats.physAtk * modifications[mods.physAtk],
        baseStats.physDef * modifications[mods.physDef],
        baseStats.specialAtk * modifications[mods.specialAtk],
        baseStats.specialDef * modifications[mods.specialDef],
        baseStats.spd * modifications[mods.spd],
    )
def calculateHPStat(hp: int, level: int) -> int:
    return math.floor(0.01 * (2 * hp) * level) + level + 10

def calculateStats(baseStats: Stats, level: int, hp=-1) -> Stats:
    hitPoints = hp
    if(hp == -1):
        hitPoints = calculateHPStat(baseStats.hp, level)
    return Stats(
        hitPoints,
        calculateStat(baseStats.physAtk, level),
        calculateStat(baseStats.physDef, level),
        calculateStat(baseStats.specialAtk, level),
        calculateStat(baseStats.specialDef, level),
        calculateStat(baseStats.spd, level),
    )



def calculateStat(stat: int, level: int) -> int:
    return math.floor(0.01 * (2 * stat) * level) + 5
def statsFromDict(jsonDict: dict):
    return Stats(jsonDict["hp"], jsonDict["physAtk"], 
            jsonDict["physDef"], jsonDict["specialAtk"],
            jsonDict["specialDef"], jsonDict["spd"]
        )

