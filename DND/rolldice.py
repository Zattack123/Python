import random
import pandas as pd
import statistics as stat


def printRollListStats(rollList):
    rollList.sort()
    rollTot = sum(rollList)
    rollAvg = rollTot/dieNumb
    rollMode = stat.mode(rollList)
    rollMedian = stat.median(rollList)
    print("Total amount Rolled: "+ str(rollTot))
    print("Average # Rolled: " + str(rollAvg))
    print("Most Common Roll: " + str(rollMode))
    print("Middle Roll: " + str(rollMedian))
    print("Your Rolls: "+ str(rollList)+"\n")


def roll(dieNumb, size):
    rollList = []
    for x in range(0,dieNumb):
        roll = random.randint(1,size)
        #doubleRoll = (random.randint(1,6),random.randint(1,6))
        #rollTot += (doubleRoll[0] + doubleRoll[1])
        rollList.append(roll)
    return rollList

def dropRoll(rollList, dropNum):
    for x in range(0,dropNum):
        rollList.remove(min(rollList))


if __name__ == "__main__":
    dice = input("\nWhat would you like to roll? (xdy)\n")
    while(dice != "q"):
        dice = dice.split('d')
        dieNumb = int(dice[0])
        size = int(dice[1])
        newRollList = roll(dieNumb, size)
        printRollListStats(newRollList)
        dropRoll(newRollList, 1)
        printRollListStats(newRollList)
        dice = input("\nWhat would you like to roll? (xdy)\n")
