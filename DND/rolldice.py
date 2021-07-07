import random
import pandas as pd
import statistics as stat


def updateRollListStats(rollListDict, printFlag):
    rollListDict["rollList"].sort()
    rollListDict["rollTot"] = sum(rollListDict["rollList"])
    rollListDict["rollAvg"] = rollListDict["rollTot"]/rollListDict["dieNumb"]
    rollListDict["rollMode"] = stat.mode(rollListDict["rollList"])
    rollListDict["rollMedian"] = stat.median(rollListDict["rollList"])
    if(printFlag):
        print("Total amount Rolled: "+ str(rollListDict["rollTot"]))
        print("Average # Rolled: " + str(rollListDict["rollAvg"]))
        print("Most Common Roll: " + str(rollListDict["rollMode"]))
        print("Middle Roll: " + str(rollListDict["rollMedian"]))
        print("Dropped Rolls: " + str(rollListDict["dropNum"]))
        print("Your Rolls: "+ str(rollListDict["rollList"])+"\n")


def roll(dieNumb, size):
    rollListDict = {"dieNumb": dieNumb, "size": size, "rollList": [], "dropNum": 0}
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
    rollListDict["dropNum"] += dropNum


if __name__ == "__main__":
    dice = input("\nWhat would you like to roll? (xdy)\n")
    while(dice != "q"):
        dice = dice.split('d')
        dieNumb = int(dice[0])
        size = int(dice[1])
        newRollListDict = roll(dieNumb, size)
        printFlag = input("\nPrint? (y/n) ")
        if((printFlag=="y") or (printFlag=="Y")):
            printFlag2 = True
        else:
            printFlag2 = False
        updateRollListStats(newRollListDict, printFlag2)
        dropNum = input("Drop any Dice? ")
        dropNum = int(dropNum)
        if(dropNum):
            dropRoll(newRollListDict, dropNum)
            updateRollListStats(newRollListDict, True)
        #print(newRollListDict.items())
        dice = input("\nWhat would you like to roll? (xdy)\n")
    print("Bye!")
