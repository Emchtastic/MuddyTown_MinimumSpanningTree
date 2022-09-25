import random, re
from Town import Town
from Street import Street
from House import House
from Graph import Graph

town = Town("", [],0)
s = 0


def randomNumber():
    a = 32
    c = 12
    m = 43
    global s

    s = (a * s + c) % m

    return s


def writeTown(fileName):
    file = open(fileName, "w")
    file.write("MuddyTown\n")
    for street in town.streets:
        file.write(str(street.weight) + ', "' + street.house1 + '",' + ' "' + street.house2 + '"\n')

def printTown():
    print(town.name)
    for street in town.streets:
        print(str(street.weight) + ", " + street.house1 + ", " + street.house2)

def readTown(name):
    houses = []
    file = open(name, "r")
    town.name = file.readline()
    for line in file:
        if not line:
            break
        var = re.split('; |, |\*|\n', line)

        street = Street(int(var[0]), var[1].replace('"', ""), var[2].replace('"', ""))
        town.streets.append(street)
        if street.house1 not in houses:
            houses.append(street.house1)
        if street.house2 not in houses:
            houses.append(street.house2)
        town.houses = houses
        town.numHouses = len(houses)

def readPavingPlan():
    planStreets = []
    totalCost = 0
    filename = input("Enter file name with paving plan")
    file = open(filename, "r")
    for line in file:
        if not line:
            break
        var = re.split('; |, |\*|\n', line)
        house1 = var[0].replace('"', "")
        house2 = var[1].replace('"', "")
        """
        if house1 not in planHouses:
            planHouses.append(house1)
        if house2 not in planHouses:
            planHouses.append(house2)
        """
        for street in town.streets:
            if house1 == street.house1 and house2 == street.house2:
                planStreets.append(Street(street.weight, house1, house2))
                totalCost += street.weight
                break

    print("Total cost of " + filename + ": " + str(totalCost))



def generateTown():
    randomNumbers = []
    houses = []
    roadType = ["St", "Ct", "Ave", "Ln", "Dr", "Way"]
    streetNames = open("names.txt").read().splitlines()

    for i in range(100):
        num = randomNumber()
        randomNumbers.append(num)

    numberOfHouses = 7  # random.choice(randomNumbers)
    town.numHouses = numberOfHouses

    for i in range(numberOfHouses):
        name = str(random.randint(1, 9999)) + " " + random.choice(streetNames).capitalize() + " " + random.choice(
            roadType)
        town.houses.append(name)
        houses.append(House(name))

    for i in houses:
        passThrough = False
        while i.availableNeighbors != 0 and passThrough == False:
            # best case
            for j in houses:
                if i.name == j.name:
                    pass
                elif i.availableNeighbors == 0:
                    break
                elif not j.connected:
                    i.addNeighbor(j.name)
                    j.addNeighbor(i.name)
                    street = Street(random.randint(1, 100), i.name, j.name)
                    town.streets.append(street)
            # If all houses have been connected but
            for j in houses:
                if i.name == j.name:
                    pass
                elif i.availableNeighbors == 0 :
                    break
                elif j.availableNeighbors != 0 and i.name not in j.neighbors:
                    i.addNeighbor(j.name)
                    j.addNeighbor(i.name)
                    street = Street(random.randint(1, 100), i.name, j.name)
                    town.streets.append(street)
            passThrough = True

    return town

