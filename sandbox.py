import json
import pokemonClass
from slowedText import sprint, sinput
from wildBattle import battle
import movesetClass
from parseDialogue import dialogue
from trainerClass import Trainer
pokemonsFile = open('pokemons.json')
pokemons = json.load(pokemonsFile)
squirtle = pokemonClass.pokemonFromDict(pokemons["squirtle"])
charmander = pokemonClass.pokemonFromDict(pokemons["charmander"])
player = Trainer("Nack")
player.addToParty(squirtle)
player.addToParty(charmander)

opponent = pokemonClass.pokemonFromDict(pokemons["bulbasaur"])
battle(player, opponent)
player.displayParty()