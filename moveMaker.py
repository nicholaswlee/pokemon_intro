from movesetClass import MoveInfo, Move, MoveSet
import random
import json
from slowedText import sinput, sprint
from pokemonClass import Pokemon
import math

def printMoves(moves: MoveSet):
    moves_list = moves.moves
    for i in range(len(moves_list)):
        sprint("\t" + str(i + 1) + ". " + moves_list[i].name)
def applyTargetStatusMove(move: Move, user, target):
    if(random.random() < move.accuracy):
        statsResponse = target.applyStatChanges(move.info.statMods, target.name)
        sprint("{name} used {move}! ".format(name=user.name, move=move.name) + statsResponse)
    else:
        sprint("{name} tried to use {move}, but it missed!".format(name=user.name, move=move.name))
    
def applyUserStatusMove(move: Move, user, target):
    if(random.random() < move.accuracy):
        statsResponse = user.applyStatChanges(move.info.statMods, user.name)
        sprint("{name} used {move}! ".format(name=user.name, move=move.name) + statsResponse)
    else:
        sprint("{name} tried to use {move}, but it missed!".format(name=user.name, move=move.name))

def calculateTypeAdvantages(moveType, type1, type2):
    modifier = 1
    if(moveType in type1["weaknesses"]):
        modifier = modifier * 2
    elif(moveType in type1["resistance"]):
        modifier = modifier * 0.5
    elif(moveType in type1["immunities"]):
        modifier = modifier * 0
    if(type2 != None):
        if(moveType in type2["weaknesses"]):
            modifier = modifier * 2
        elif(moveType in type2["resistance"]):
            modifier = modifier * 0.5
        elif(moveType in type2["immunities"]):
            modifier = modifier * 0
    return modifier
def calculateStab(move: Move, user: Pokemon):
    stab = 1
    if(user.type1 == move.type):
        stab = 1.5
    elif(user.type2 != None):
        if(user.type2 == move.type):
            stab = 1.5
    return stab

def physicalDamage(modifier, move: Move, user: Pokemon, target: Pokemon):
    stab = calculateStab(move, user)
    damage = ((((2*user.level/5 + 2) * move.info.basePower * (user.battleStats.physAtk/target.battleStats.physDef))/50) + 2) * modifier * stab
    return damage

def specialDamage(modifier: int, move: Move, user: Pokemon, target: Pokemon):
    stab = calculateStab(move, user)
    damage = ((((2 * user.level/5 + 2) * move.info.basePower * (user.battleStats.specialAtk / target.battleStats.specialDef))/50) + 2) * modifier * stab
    return damage

def effectivenessPhrase(modifier):
    if modifier == 1:
        return ""
    elif modifier < 1:
        return "It wasn't very effective. "
    elif modifier > 1:
        return "It was super effective! "
def damageTarget(move: Move, user, target):
    if(random.random() < move.accuracy):
        typesFile = open('typeChart.json')
        types = json.load(typesFile)
        type1 = types[target.type1]
        type2 = None if (target.type2 == None) else types[target.type2]
        modifier = calculateTypeAdvantages(move.type, type1, type2)
        damage = 0
        if(move.category == "special"):
            damage = specialDamage(modifier, move, user, target)
        elif(move.category == "physical"):
            damage = physicalDamage(modifier, move, user, target)
        damage = math.floor(damage)
        target.applyDamage(damage)

        effectivenessString = effectivenessPhrase(modifier)
        sprint("{name} used {move}! ".format(name=user.name, move=move.name) + effectivenessString + "It did {damage} damage".format(damage=damage))
    else:
        sprint("{name} tried to use {move}, but it missed!".format(name=user.name, move=move.name))
def useMove(move, user, target):
    '''
    Uses move on target. Assume user can use move
    '''
    category = move.category
    if(category == "statusTarget"):
        applyTargetStatusMove(move, user, target)
    elif(category ==  "statusSelf"):
        applyUserStatusMove(move, user, target)
    else:
        damageTarget(move, user, target)