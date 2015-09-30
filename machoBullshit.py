#!/usr/bin/python
import dice
import os
from pandas import *
if(os.name == "posix"):
	tmp = os.system('clear')
else:
	tmp = os.system('cls')
print("Welcome to Unbelieveable Macho Bullshit!")
class Player:
	name = ""
	character = ""
	bio = ""
	mind = ""
	edu = ""
	mooks = ""
	hench = ""
	muscle = ""
	train = ""
	dead = False
def biggest(players):
	max = 1
	index = 0
	for player in players:
		if (player.muscle > max):
			index = players.index(player)
	return index
def turn(players, current):
	points = 2;
	while(points>0):
		mind = input("How many points would you like to add to mind?: ")
		current.mind = current.mind + mind
		points = points - mind
		if(points > 0):
			mooks = input("How many points would you like to add to mooks?: ")
			current.mooks = current.mooks + mooks
			points = points - mooks
		if(points > 0):
			muscle = input("How many points would you like to add to muscle?: ")
			current.muscle = current.muscle + muscle
			points = points - muscle
	input("Describe your evil deed (Enter to continue)")
	players.remove(current)
	print("Describe the hero")
players = []
last = ""
xls = ExcelFile('test.xlsx')
df = xls.parse(xls.sheet_names[0])
data = df.to_dict()
for i in range(0, len(data["Name"])):
	player = Player()
	player.name = data["Name"][i]
	player.character = data["Character"][i]
	player.bio = data["Description"][i]
	player.mind = data["Mind"][i]
	player.edu = data["Education"][i]
	player.mooks = data["Mooks"][i]
	player.hench = data["Henchmen"][i]
	player.muscle = data["Muscle"][i]
	player.train = data["Training"][i]
	players.append(player)
print("")
big = players[biggest(players)]
bigstr = big.character + "(" + big.name + ") " + "is the largest motherfucker in the room and gets to go first!"
print(bigstr)
turn(players, big)
