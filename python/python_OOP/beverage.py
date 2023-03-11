from plastic import *
def buildLines(word,num):
    count = 0
    if word == "":
        count = num
        print(word, end="")
    elif num > len(word):
        count = num - len(word)
        print(word, end="")

    else:
        count = len(word)

    for i in range(count):
        print("-",end="")
        if i == count-1:
            print("-")
class bottle(plastic):
    def __init__(self, material, bottleSize):
        self.material = material
        self.bottleSize = bottleSize
        self.disposal = "" # bring the info from plastic.py


    def getMaterialBottle(self):
        return self.material
    def getBottleSize(self):
        return self.bottleSize
    def setMaterial(self,user):
        self.material = user
    def setBottleSize(self,user):
        self.bottleSize = user
    def disposal():
        pass


class beverage(bottle):
    def __init__(self,category, cost, material, bottleSize):
        self.category = category
        self.cost = cost
        super().__init__(material.upper(), bottleSize)

    def getCategory(self):
        return self.category
    def getCost(self):
        return self.cost
    
    def displayInfoBeverage(self):
        print("🚩 ",end="")
        buildLines(self.category,20)
        print(f"\tCost: {beverage.getCost(self)} baht")
        print(f"\tVol: {bottle.getBottleSize(self)}")
        print(f"\tMaterial: {bottle.getMaterialBottle(self)}")
        

    
oneDrink = beverage("Soda",10,"PET", 200)
oneDrink.displayInfoBeverage()