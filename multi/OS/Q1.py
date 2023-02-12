import threading as th

NAME = [["Sasipa", "Boon-umchu"], 
        ["Kanpitcha", "Hong-ek"], 
        ["Phattrada", "Mikota"],
        ["Nichapa", "Pornpattanadul"]]

def main():
    print(countLetter())

def displayFullname():
    for i in range(len(NAME)):
        print(NAME[i])
def displayFullnameReverse():
    pass
def asciiToInt():
    pass

def countLetter():
    total = 0
    for i in range(len(NAME)):
        for j in range(2):
            print(NAME[i][j])
            total += len(NAME[i][j])

    return total

main()