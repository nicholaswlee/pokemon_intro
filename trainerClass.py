
from pokemonClass import Pokemon
from typing import List
from slowedText import sprint, sinput
from bagClass import Bag, Ball, Potion

class Trainer:
    def __init__(self, name, party: List[Pokemon] = [], pokedollar=0) -> None:
        self.name = name
        self.party = party
        self.partySize = len(party)
        self.pokedollar = pokedollar
        self.box = []
        self.activePokemon = None
        self.bag = Bag()
    def addToParty(self, pokemon: Pokemon):
        if self.partySize == 6:
            self.displayParty()
            sprint('\t 7. ' + pokemon.name)
            index = sinput("Please select what pokemon you would like to remove")
            if index == 7:
                self.box.append(pokemon)
                sprint(pokemon.name + " has been sent to the box.")
            else:
                self.removeParty(index)
                self.addToParty(pokemon)
        else:
            sprint(pokemon.name + " has been added to the party")
            self.party.append(pokemon)
            self.partySize += 1
        self.activePokemon = self.party[0]
    def retrivePokemon(self, index):
        return self.party[index - 1]
    def displayParty(self):
        sprint("Here is your party")
        for i in range(self.partySize):
            sprint('\t' + str(i + 1) + ". " + self.party[i].name + " HP: " + str(self.party[i].battleStats.hp) + "/" + str(self.party[i].currentStats.hp))
    def removeParty(self, index):
        pokemon = self.party.pop(index - 1)
        self.partySize -= 1
        self.box.append(pokemon)
        sprint(pokemon.name)
    def giveBalls(self, type: str, count: int):
        self.bag.balls[type] += count
    def useBall(self, type: str):
        self.bag.balls[type] -= 1
        
