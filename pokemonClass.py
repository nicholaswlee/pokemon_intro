
from statsClass import Stats, StatsStages, calculateBattleStats, calculateStats, statsFromDict;
from movesetClass import MoveSet, learnMoveSetFromLevels
from slowedText import sprint
baseStats = {
    "hp" : 50,
    "physAtk" : 10,
    "specialAtk" : 10,
    "physDef" : 10,
    "specialDef" : 10,
    "spd" : 10,
}

class Pokemon: 
    """
    Defines a pokemon

    Attributes
    ----------
    name - 
    """
    def __init__(self, name, type1, baseStats, moves: MoveSet, type2=None, level=5):
        self.name = name
        self.level = level
        self.type1 = type1
        self.type2 = type2
        self.moves = moves
        self.baseStats = baseStats
        self.statStages = StatsStages()
        self.currentStats = calculateStats(baseStats, level)
        self.battleStats = calculateBattleStats(self.currentStats, self.statStages)

    def applyStatChanges(self, mods, name):
        response = self.statStages.applyStatMods(mods, name)
        self.battleStats = calculateBattleStats(self.currentStats, self.statStages, hp=self.battleStats.hp)
        return response
    def applyDamage(self, damage):
        self.battleStats.hp = self.battleStats.hp - damage
    def restore(self):
        self.battleStats.hp = self.currentStats.hp
    def removeBattle(self):
        self.statStages = StatsStages()
        self.battleStats = calculateBattleStats(self.currentStats, self.statStages, hp=self.battleStats.hp)
    def displayStats(self):
        sprint(
            self.name + "'s stats:" + 
            "\n\tHP: " + str(self.battleStats.hp) + "/" + str(self.currentStats.hp) + 
            "\n\tATK: " + str(self.battleStats.physAtk) +
            "\n\tSPATK: " + str(self.battleStats.specialAtk) +
            "\n\tDEF: " + str(self.battleStats.physDef) +
            "\n\tSPDEF: " + str(self.battleStats.specialDef) + 
            "\n\tSPD: " + str(self.battleStats.spd)
        )

def pokemonFromDict(jsonDict: dict, moveSet=MoveSet(), level=5):
    return Pokemon(jsonDict["name"], jsonDict["type1"], statsFromDict(jsonDict["stats"]), learnMoveSetFromLevels(jsonDict["moves"], level), type2=jsonDict["type2"],level=level)