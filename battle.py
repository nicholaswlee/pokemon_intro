from pokemonClass import Pokemon
from slowedText import sinput, sprint
from moveMaker import useMove, printMoves
import movesetClass
import random
from enum import Enum
class Result(Enum):
    PLAYER = 1
    OPPONENT = 2
    RUN = 3
    CONTINUE = 4

def battle(player, opponent):
    sprint("Go " + opponent.name + "!")
    sprint("Go " + player.name + "!")
    result = None
    while(True):
        sprint(
        "Opponent's " + opponent.name + "'s HP: " + str(opponent.battleStats.hp) +"\n" + 
            "Your " + player.name + "'s HP: " + str(player.battleStats.hp)
        )
        promptMove(player,opponent)
        result = battleStatus(player, opponent)
        if(result != Result.CONTINUE):
            break
        opponentMove(player,opponent)
        result = battleStatus(player, opponent)
        if(result != Result.CONTINUE):
            break
    battleFinish(result, player, opponent)
    return result
    

    
def promptMove(player: Pokemon, opponent: Pokemon):
    sprint("What would you like to do?")
    sprint("Here are your moves: ")
    printMoves(player.moves)
    moveIndex = int(sinput("Please select a number: ").strip())
    moveSelected = player.moves.selectMove(moveIndex);
    useMove(moveSelected, player, opponent)
    print()

def opponentMove(player: Pokemon, opponent: Pokemon):
    randomMove = random.randint(1, opponent.moves.length)
    moveSelected = opponent.moves.selectMove(randomMove);
    useMove(moveSelected, opponent, player)

def battleStatus(player: Pokemon, opponent: Pokemon):
    if(player.battleStats.hp <= 0):
        return Result.OPPONENT
    elif(opponent.battleStats.hp <= 0):
        return Result.PLAYER
    return Result.CONTINUE

def battleFinish(result, player: Pokemon, opponent: Pokemon):
    if(result == Result.OPPONENT):
        txt = "{user} has fainted. {name} has won! You lost!"
        sprint(txt.format(user=player.name, name=opponent.name))
    elif(result == Result.PLAYER):
        txt = "You won! {name} has fainted!"
        sprint(txt.format(name=opponent.name))
    player.removeBattle()
    opponent.removeBattle()


