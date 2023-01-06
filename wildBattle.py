from trainerClass import Trainer
from pokemonClass import Pokemon
from slowedText import sinput, sprint
from moveMaker import useMove, printMoves
import movesetClass
import random
from enum import Enum
import random
class Result(Enum):
    PLAYER = 1
    OPPONENT = 2
    RUN = 3
    CONTINUE = 4
    CAUGHT = 5

def battle(player: Trainer, opponent):
    player.activePokemon = player.party[0]
    sprint(opponent.name + " approaches you!")
    sprint("Go " + player.activePokemon.name + "!")
    result = None
    while(True):
        sprint(
        "Opponent's " + opponent.name + "'s HP: " + str(opponent.battleStats.hp) +"\n" + 
            "Your " + player.activePokemon.name + "'s HP: " + str(player.activePokemon.battleStats.hp)
        )
        result = promptChoice(player, opponent)
        if(result != Result.CONTINUE):
            break
        result = opponentMove(player,opponent)
        if(result != Result.CONTINUE):
            break
    battleFinish(result, player, opponent)
    return result
    

def promptChoice(player: Trainer, opponent: Pokemon):
    sprint("What would you like to do?")
    sprint("\t1. Use Pokeball")
    sprint("\t2. Use Move")
    sprint("\t3. Switch Pokemon")
    sprint("\t4. Run")
    choiceIndex = int(sinput("Please select a number: ").strip())
    if(choiceIndex == 1):
        return promptBall(player, opponent)
    elif(choiceIndex == 2):
        return promptMove(player, opponent)
    elif(choiceIndex == 3):
        return promptSwitch(player, opponent)
    elif(choiceIndex == 4):
        return run(player, opponent)

def promptBall(player: Trainer, opponent: Pokemon):
    sprint("You threw a pokeball")
    i = 0
    for i in range(3):
        x = random.random()
        sprint("  *  ", seconds = 0.2)
        if (x > 0.75):
            if(i == 0):
                sprint("It broke free!")
            elif(i == 1):
                sprint("It appeared to be caught!")
            elif(i == 2):
                sprint("Aww so close!")
            return Result.CONTINUE
    player.addToParty(opponent)
    return Result.CAUGHT

def promptSwitch(player: Trainer, opponent: Pokemon):
    index = player.partySize + 1
    while(index > player.partySize):
        sprint("Who would you like to switch " + player.activePokemon.name + " for?")
        player.displayParty()
        index = int(sinput("Please select a number: ").strip())
    player.activePokemon.removeBattle()
    player.activePokemon = player.retrivePokemon(index)
    sprint("Go " + player.activePokemon.name)
    return Result.CONTINUE

def run(player, opponent):
    return Result.RUN 

def promptMove(player: Trainer, opponent: Pokemon):
    sprint("Here are your moves: ")
    printMoves(player.activePokemon.moves)
    moveIndex = int(sinput("Please select a number: ").strip())
    moveSelected = player.activePokemon.moves.selectMove(moveIndex);
    useMove(moveSelected, player.activePokemon, opponent)
    print()
    return battleStatus(player, opponent)

def opponentMove(player: Trainer, opponent: Pokemon):
    randomMove = random.randint(1, opponent.moves.length)
    moveSelected = opponent.moves.selectMove(randomMove);
    useMove(moveSelected, opponent, player.activePokemon)
    return battleStatus(player, opponent)

def battleStatus(player: Trainer, opponent: Pokemon):
    if(player.activePokemon.battleStats.hp <= 0):
        return Result.OPPONENT
    elif(opponent.battleStats.hp <= 0):
        return Result.PLAYER
    return Result.CONTINUE

def battleFinish(result, player: Trainer, opponent: Pokemon):
    if(result == Result.OPPONENT):
        txt = "{user} has fainted. {name} has won! You lost!"
        sprint(txt.format(user=player.activePokemon.name, name=opponent.name))
    elif(result == Result.PLAYER):
        txt = "You won! {name} has fainted!"
        sprint(txt.format(name=opponent.name))
    elif(result == Result.RUN):
        sprint("You got away safely")
    elif(result == Result.CAUGHT):
        txt = "Congrats! You caught a {name}!"
        sprint(txt.format(name=opponent.name))
    player.activePokemon.removeBattle()
    opponent.removeBattle()


