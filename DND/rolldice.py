import random
import pandas as pd
import statistics as stat


def updateRollListStats(rollListDict):
    rollListDict["rollList"].sort()
    rollListDict["rollTot"] = sum(rollListDict["rollList"])
    rollListDict["rollAvg"] = rollListDict["rollTot"]/rollListDict["dieNumb"]
    rollListDict["rollMode"] = stat.mode(rollListDict["rollList"])
    rollListDict["rollMedian"] = stat.median(rollListDict["rollList"])
    print("Total amount Rolled: "+ str(rollListDict["rollTot"]))
    print("Average # Rolled: " + str(rollListDict["rollAvg"]))
    print("Most Common Roll: " + str(rollListDict["rollMode"]))
    print("Middle Roll: " + str(rollListDict["rollMedian"]))
    print("Your Rolls: "+ str(rollListDict["rollList"])+"\n")


def roll(dieNumb, size):
    rollListDict = {"dieNumb": dieNumb, "size": size, "rollList": []}
    for x in range(0,dieNumb):
        roll = random.randint(1,size)
        #doubleRoll = (random.randint(1,6),random.randint(1,6))
        #rollTot += (doubleRoll[0] + doubleRoll[1])
        rollListDict["rollList"].append(roll)
    return rollListDict

def dropRoll(rollListDict, dropNum):
    for x in range(0,dropNum):
        #rollListDict["rollTot"] -= min(rollListDict["rollList"])
        rollListDict["dieNumb"] -= 1
        rollListDict["rollList"].remove(min(rollListDict["rollList"]))



if __name__ == "__main__":
    dice = input("\nWhat would you like to roll? (xdy)\n")
    while(dice != "q"):
        dice = dice.split('d')
        dieNumb = int(dice[0])
        size = int(dice[1])
        newRollListDict = roll(dieNumb, size)
        updateRollListStats(newRollListDict)
        dropRoll(newRollListDict, 1)
        updateRollListStats(newRollListDict)
        #print(newRollListDict.items())
        dice = input("\n\nWhat would you like to roll? (xdy)\n")
