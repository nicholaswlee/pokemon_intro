import json
import pokemonClass
from slowedText import sprint, sinput
import battle
import movesetClass
from parseDialogue import dialogue
from trainerClass import Trainer
def rivalBattle():
    starters = {
        1 : "bulbasaur",
        2 : "charmander",
        3 : "squirtle"
    }
    keyVariables = dict()
    print('''
\n                                  ,'\\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|''')
    dialogue("intro1.json", variables=keyVariables)
    dialogue("intro2.json", variables=keyVariables)
    player = Trainer(keyVariables["PLAYER_NAME"])
    rival = Trainer(keyVariables["RIVAL_NAME"])
    dialogue("intro3.json", variables=keyVariables)
    pokemonsFile = open('pokemons.json')
    pokemons = json.load(pokemonsFile)
    starterMap = pokemons[keyVariables["STARTER_NAME"]]
    rivalMap = pokemons[keyVariables["RIVAL_STARTER_NAME"]]

    starter = pokemonClass.pokemonFromDict(starterMap)
    player.addToParty(starter)

    opponent = pokemonClass.pokemonFromDict(rivalMap)
    rival.addToParty(opponent)

    result = battle.battle(starter, opponent)
    keyVariables["RESULT"] = result
    starter.restore()
    dialogue("intro4.json", variables=keyVariables)
    
rivalBattle()



        