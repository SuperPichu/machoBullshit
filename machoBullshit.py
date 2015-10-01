#!/usr/bin/python
import dice
import os
from pandas import *
from time import sleep

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
	full = ""
	dead = False
def clear():
	if(os.name == "posix"):
		tmp = os.system('clear')
	else:
		tmp = os.system('cls')
def biggest(players):
	max = 1
	index = 0
	for player in players:
		if (player.muscle > max):
			index = players.index(player)
	return index
def roll(num, top, bottom):
	result = []
	rolls = dice.roll(str(num) + 'd6')
	success = 0
	fail = 0
	for die in rolls:
		if(die <= bottom ):
			fail += 1
		else if(die >= top):
			success += 1
	result.append(success)
	result.append(fail)
	return result
def dead(player):
	clear()
	print(player.full + " is dying!!")
	print("Shout a one-liner to finish them off!")
	sleep(10)
	valid = False
	while(!valid):
		answer = input("Times up! Are they dead? [Y/N]")
		if(answer == "Y" || answer == "y"):
			valid = True
			player.dead = True
			print(player.full + " is DEAD!")
		if(answer == "N" || answer == "n"):
			valid = True
	return
def showdown(player):
	clear()
	print("Final Showdown!")
	result = roll(player.mind, 6, 5)
	player.mind -= result[1]
	if(player.mind == 0){
		dead(player)
		return
	}
	result = roll(player.mooks, 5, 4)
	player.mooks -= result[1]
	if(player.mooks == 0){
		dead(player)
		return
	}
	result = roll(player.muscle, 4, 3)
	player.muscle -= result[1]
	if(player.muscle == 0){
		dead(player)
		return
	}
	print("You Survive!")
	return
def stats(players):
	clear()
	for player in players:
		print("Player: " + player.full)
		print("Mind: " + str(player.mind))
		print("Mooks: " + str(player.mooks))
		print("Muscle: " + str(player.muscle))
		dead = "No"
		if(player.dead):
			dead = "Yes"
		print("Dead?: " + dead)
def startup(players):
	clear()
	for player in players:
		print("Player: " + player.full)
		print("\t" + player.bio)
		print("Mind: " + str(player.mind))
		print("\t" + player.edu)
		print("Mooks: " + str(player.mooks))
		print("\t" + player.hench)
		print("Muscle: " + str(player.muscle))
		print("\t" + player.train)
		input("Press Enter to Continue")
		clear()
def nextPlayer(players, last):
	valid = False
	clear()
	top = len(players)
	for i in range(0, top):
		print(str(i+1) + "." + players[i].full)
	while(!valid):
		answer = input("Choose next player: ")
		if(answer > 0 && answer <= top):
			valid = True
			answer -= 1
			players.append(last)
			current = players[i]
			stats(players)
			turn(players, current)
def turn(players, current):
	clear()
	print(current.full)
	players.remove(current)
	points = 2;
	while(points>0):
		print(points + " points remaining")
		mind = input("How many points would you like to add to mind?: ")
		current.mind += mind
		points -= mind
		if(points > 0):
			mooks = input("How many points would you like to add to mooks?: ")
			current.mooks += mooks
			points -= mooks
		if(points > 0):
			muscle = input("How many points would you like to add to muscle?: ")
			current.muscle += muscle
			points -= muscle
	if(!current.dead):
		input("Describe your evil deed (Enter to continue)")
		print("Describe the hero and set his relentlessness")
		hero = 0
		for player in players:
			print(player.name)
			valid = False
			mind = 0
			mooks = 0
			muscle = 0

			while(!valid):
				mind = input("How many mind dice will you contribute?: ")
				valid = (mind <= player.mind)
			result = roll(mind, 5, 1)
			hero += result[0]
			player.mind -= result[1]
			print(str(result[0]) + " successes!")
			print(str(player.mind) + " mind remaining")
			if(player.mind == 0):
				dead(player)
			valid = False
			while(!valid):
				mooks = input("How many mooks dice will you contribute?: ")
				valid = (mooks <= player.mooks)
			result = roll(mooks, 5, 1)
			hero += result[0]
			player.mooks -= result[1]
			print(str(result[0]) + " successes!")
			print(str(player.mooks) + " mooks remaining")
			if(player.mooks == 0):
				dead(player)
			valid = False
			while(!valid):
				muscle = input("How many muscle dice will you contribute?: ")
				valid = (muscle < player.muscle)
			result = roll(muscle, 5, 1)
			hero += result[0]
			player.muscle -= result[1]
			print(str(result[0]) + " successes!")
			print(str(player.muscle) + " muscle remaining")
			if(player.muscle == 0):
				dead(player)
		input("The hero has a relentlessness of " + str(hero))
		valid = False
		finished = False
		options = ["1. Mind", "2. Mooks", "3. Muscle"]
		while(!valid):
			clear()
			print(current.full)
			print("")
			print("")
			for option in options:
				print(option)
			answer = input("Which will you wager?: ")
			if(answer > 0 && answer < 4):
				valid = True
				valid2 = False
				amt = 0
				if(answer = 1):
					while(!valid2):
						amt = input("How many dice will you wager?: ")
						valid2 = (amt <= current.mind)
					result = roll(amt, 4, 3)
					current.mind -= result[1]
					print(str(result[0]) + "successes!")
					input(str(current.mind) + " mind remaining")
					if(result[0] < hero):
						showdown(current)
					else:
						print("You Survive!")
				else if(answer = 2):
					while(!valid2):
						amt = input("How many dice will you wager?: ")
						valid2 = (amt <= current.mooks)
					result = roll(amt, 5, 4)
					current.mooks -= result[1]
					print(str(result[0]) + "successes!")
					input(str(current.mooks) + " mooks remaining")
					if(result[0] < hero):
						showdown(current)
					else:
						print("You Survive!")
				else if(answer = 3):
					while(!valid2):
						amt = input("How many dice will you wager?: ")
						valid2 = (amt <= current.muscle)
					result = roll(amt, 6, 5)
					current.muscle -= result[1]
					print(str(result[0]) + "successes!")
					input(str(current.muscle) + " muscle remaining")
					if(result[0] < hero):
						showdown(current)
					else:
						print("You Survive!")
	nextPlayer(players, current)

clear()
input("Welcome to Unbelieveable Macho Bullshit!")
players = []
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
	player.full = player.character + "(" + player.name + ")"
	players.append(player)
startup(players)
big = players[biggest(players)]
print(big.full + " is the largest motherfucker in the room and gets to go first!")
turn(players, big)
