

class creature:

    def __init__(self, str, dex, con, int, wis, cha, name, race, dndClass, level):
        self.str = str
        self.strMod = (str-10)//2
        self.dex = dex
        self.dexMod = (dex-10)//2
        self.con = con
        self.conMod = (con-10)//2
        self.int = int
        self.intMod = (int-10)//2
        self.wis = wis
        self.wisMod = (wis-10)//2
        self.cha = cha
        self.chaMod = (wis-10)//2

        self.name = name
        self.race = race
        self.dndClass = dndClass
        self.level = level


    def __str__(self):
        return f"{self.name} the level {self.level} {self.race} {self.dndClass}"

    def printStatBlock(self):
        print(self)
        print("STR: " + str(self.str) + " (+" + str(self.strMod) + ")")
        print("DEX: " + str(self.dex) + " (+" + str(self.dexMod) + ")")
        print("CON: " + str(self.con) + " (+" + str(self.conMod) + ")")
        print("INT: " + str(self.int) + " (+" + str(self.intMod) + ")")
        print("WIS: " + str(self.wis) + " (+" + str(self.wisMod) + ")")
        print("CHA: " + str(self.cha) + " (+" + str(self.chaMod) + ")")




if __name__ == "__main__":
    TestCreature = creature(10,11,12,13,14,15, "Zach", "Elf", "Ranger", 20)
    TestCreature.printStatBlock()
