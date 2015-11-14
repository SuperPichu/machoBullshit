#!/usr/bin/python
import dice
import os
from pandas import *
from time import sleep


class Player:
    def __init__(self):
        pass

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
    if os.name == "posix":
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
        if die <= bottom:
            fail += 1
        elif die >= top:
            success += 1
    result.append(success)
    result.append(fail)
    return result


def dead(player):
    clear()
    print(player.full + " is dying!!")
    print("Shout a one-liner to finish them off!\nPlease wait...")
    sleep(10)
    valid = False
    while not valid:
        answer = raw_input('Times up! Are they dead? [Y/N]: ')
        if (answer == "Y") or (answer == "y"):
            valid = True
            player.dead = True
            print(player.full + " is DEAD!")
        if (answer == "N") or (answer == "n"):
            valid = True
    raw_input("Press Enter to Continue")
    return


def showdown(player):
    clear()
    print("Final Showdown!")
    result = roll(player.mind, 6, 5)
    player.mind -= result[1]
    if player.mind == 0:
        dead(player)
        return
    result = roll(player.mooks, 5, 4)
    player.mooks -= result[1]
    if player.mooks == 0:
        dead(player)
        return
    result = roll(player.muscle, 4, 3)
    player.muscle -= result[1]
    if player.muscle == 0:
        dead(player)
        return
    print("You Survive!")
    raw_input("Press Enter to Continue")
    return


def stats(players):
    clear()
    for player in players:
        print("Player: " + player.full)
        print("Mind: " + str(player.mind))
        print("Mooks: " + str(player.mooks))
        print("Muscle: " + str(player.muscle))
        dead = "No"
        if player.dead:
            dead = "Yes"
        print("Dead?: " + dead)
        print("\n\n")
    raw_input("Press Enter to Continue")


def startup(players):
    clear()
    for player in players:
        print("Player: " + player.full)
        print(player.bio + "\n\n")
        print("Mind: " + str(player.mind))
        print(player.edu + "\n\n")
        print("Mooks: " + str(player.mooks))
        print(player.hench + "\n\n")
        print("Muscle: " + str(player.muscle))
        print(player.train + "\n\n")
        raw_input("Press Enter to Continue")
        clear()


def nextPlayer(players, last):
    valid = False
    clear()
    top = len(players)
    for i in range(0, top):
        print(str(i + 1) + "." + players[i].full)
    while not valid:
        answer = int(raw_input("Choose next player: "))
        if (answer > 0) and (answer <= top):
            valid = True
            answer -= 1
            current = players[answer]
            players.append(last)
            stats(players)
            turn(players, current)


def turn(players, current):
    clear()
    print(current.full)
    players.remove(current)
    points = 2
    while points > 0:
        print(str(points) + " points remaining")
        mind = int(raw_input("How many points would you like to add to mind?: "))
        if mind > 2:
            mind = 2
        current.mind += mind
        points -= mind
        if points > 0:
            mooks = int(raw_input("How many points would you like to add to mooks?: "))
            if mooks > 2:
                mooks = 2
            current.mooks += mooks
            points -= mooks
        if points > 0:
            muscle = int(raw_input("How many points would you like to add to muscle?: "))
            if muscle > 2:
                muscle = 2
            current.muscle += muscle
            points -= muscle
    if not current.dead:
        raw_input("Describe your evil deed (Enter to continue)")
        clear()
        print("Describe the hero and set his relentlessness")
        hero = 0
        for player in players:
            print(player.full)
            valid = False
            mind = 0
            mooks = 0
            muscle = 0

            while not valid:
                mind = int(raw_input("How many mind dice will you contribute?: "))
                valid = (mind <= player.mind)
            result = roll(mind, 5, 1)
            hero += result[0]
            player.mind -= result[1]
            print(str(result[0]) + " successes!")
            print(str(player.mind) + " mind remaining")
            if player.mind == 0:
                dead(player)
            valid = False
            while not valid:
                mooks = int(raw_input("How many mooks dice will you contribute?: "))
                valid = (mooks <= player.mooks)
            result = roll(mooks, 5, 1)
            hero += result[0]
            player.mooks -= result[1]
            print(str(result[0]) + " successes!")
            print(str(player.mooks) + " mooks remaining")
            if player.mooks == 0:
                dead(player)
            valid = False
            while not valid:
                muscle = int(raw_input("How many muscle dice will you contribute?: "))
                valid = (muscle <= player.muscle)
            result = roll(muscle, 5, 1)
            hero += result[0]
            player.muscle -= result[1]
            print(str(result[0]) + " successes!")
            print(str(player.muscle) + " muscle remaining")
            if player.muscle == 0:
                dead(player)
            raw_input("Press Enter to Continue")
            clear()
        raw_input("The hero has a relentlessness of " + str(hero))
        valid = False
        options = ["1. Mind(" + str(current.mind) + ")", "2. Mooks(" + str(current.mooks) + ")",
                   "3. Muscle(" + str(current.muscle) + ")", "4. FINAL SHOWDOWN"]
        while not valid:
            clear()
            print(current.full)
            print("")
            print("")
            for option in options:
                print(option)
            answer = int(raw_input("Which will you wager?: "))
            if (answer > 0) and (answer < 5):
                valid = True
                valid2 = False
                amt = 0
                if answer == 1:
                    while not valid2:
                        amt = int(raw_input("How many dice will you wager?: "))
                        valid2 = (amt <= current.mind)
                    result = roll(amt, 4, 3)
                    current.mind -= result[1]
                    print(str(result[0]) + " successes!")
                    raw_input(str(current.mind) + " mind remaining")
                    if result[0] < hero:
                        showdown(current)
                    else:
                        print("You Survive!")
                elif answer == 2:
                    while not valid2:
                        amt = int(raw_input("How many dice will you wager?: "))
                        valid2 = (amt <= current.mooks)
                    result = roll(amt, 5, 4)
                    current.mooks -= result[1]
                    print(str(result[0]) + "successes!")
                    raw_input(str(current.mooks) + " mooks remaining")
                    if result[0] < hero:
                        showdown(current)
                    else:
                        print("You Survive!")
                elif answer == 3:
                    while not valid2:
                        amt = int(raw_input("How many dice will you wager?: "))
                        valid2 = (amt <= current.muscle)
                    result = roll(amt, 6, 5)
                    current.muscle -= result[1]
                    print(str(result[0]) + "successes!")
                    raw_input(str(current.muscle) + " muscle remaining")
                    if result[0] < hero:
                        showdown(current)
                    else:
                        print("You Survive!")
                elif answer == 4:
                    showdown(current)
    nextPlayer(players, current)


clear()
raw_input("Welcome to Unbelievable Macho Bullshit!")
players = []
xls = ExcelFile('characters.xlsx')
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
