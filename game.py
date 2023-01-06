import json
from pokemonClass import Pokemon


def runGame():
    """
    Runs the game
    """
    print("Welcome to the world of pokemon!")
    print("Game running")
    typesFile = open('typeChart.json')
    types = json.load(typesFile)
    pikachu = Pokemon("Charmander", types["fire"], level=10);
    
    print(pikachu.type1, pikachu.name, pikachu.level, pikachu.stats["physAtk"])

runGame()

    