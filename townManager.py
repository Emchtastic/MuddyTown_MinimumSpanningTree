import random
import re
import time

from Street import Street
from House import House
from Town import Town

minimumCost = 5  # starting minimum for MiniTown
s = 0
standardFormat = True

"""
Method to create a random number using Skiena's linear congruential generator
"""


def randomNumber():
    a = 1664525
    c = 1013904223
    m = 2 ** 32
    global s

    s = (a * s + c) % m

    return round(s / 100000000)


"""Creates two int lists populated by randomNumber() and python's Random.randInt(). Compares the execution times and 
distributions. """


def compareNumGenerators():
    randomNums = []
    randomPythonNums = []
    start = time.perf_counter()
    for i in range(100):
        num = randomNumber()
        randomNums.append(num)
    stop = time.perf_counter()
    print(f"My RNG completed in {stop - start:0.9f} seconds")
    start = time.perf_counter()
    for i in range(100):
        pyNum = random.randint(1, 50)
        randomPythonNums.append(pyNum)
    stop = time.perf_counter()
    print(f"Python RNG completed in {stop - start:0.9f} seconds")

    counters = [[], [], [], [], []]
    for num in randomNums:
        if 0 <= num <= 9:
            counters[0] += "*"
        elif 10 <= num <= 19:
            counters[1] += "*"
        elif 20 <= num <= 29:
            counters[2] += "*"
        elif 30 <= num <= 39:
            counters[3] += "*"
        elif 40 <= num <= 49:
            counters[4] += "*"

    pyCounters = [[], [], [], [], []]
    for pyNum in randomPythonNums:
        if 0 <= pyNum <= 9:
            pyCounters[0] += "*"
        elif 10 <= pyNum <= 19:
            pyCounters[1] += "*"
        elif 20 <= pyNum <= 29:
            pyCounters[2] += "*"
        elif 30 <= pyNum <= 39:
            pyCounters[3] += "*"
        elif 40 <= pyNum <= 49:
            pyCounters[4] += "*"

    i = 0
    j = 0
    print("\npseudorandom number generator results:")
    for count in counters:
        print(str(i) + ": " + "".join(count))
        i += 1
    print("\nPython RNG results:")
    for count in pyCounters:
        print(str(j) + ": " + "".join(count))
        j += 1


"""Street values from passed town object and written to file. Standard format depends on last used format, i.e. what format was read in last"""


def writeTown(town, file):
    file = open(file, "w")
    if standardFormat:
        file.write("\"" + town.name + "\"" + "\n")
        for street in town.streets:
            file.write(str(street.cost) + ',"' + street.house1 + '",' + '"' + street.house2 + '"\n')
    else:
        file.write("Name: " + town.name.replace("\"", "") + "\n")
        file.write("Number of Buildings: " + str(town.numHouses) + "\n")
        i = 1
        for house in town.houses:
            file.write("[" + str(i) + "] " + house + "\n")
            i += 1
        file.write("=====" + "\n")
        file.write(str(town.numHouses) + " " + str(len(town.streets)) + "\n")
        for street in town.streets:
            file.write(
                str(town.houses.index(street.house1) + 1) + " " + str(town.houses.index(street.house2) + 1) + " " + str(
                    street.cost) + "\n")


"""
If the paving plan is coming from Prim's, write the passed street values to write.
"""


def writePavingPlan(file, planName, pavingPlan):
    file = open(file, "w")
    file.write("\"" + planName.replace("\"", "") + "\"" + "\n")
    for street in pavingPlan[1:]:
        file.write(street + "\n")


"""
Displays town in either standard or alternative format. O(s+b) for alternative, O(s) for standard.
"""


def printTown(town, printFormat=1):
    match printFormat:
        case 1:
            print("\"" + town.name + "\"")
            for street in town.streets:
                print(str(street.cost) + ",\"" + street.house1 + "\",\"" + street.house2 + "\"")
        case 2:
            print("Name: " + town.name.replace("\"", "") + "\n"
                                                           "Number of Buildings: " + str(town.numHouses))
            for house in town.houses:
                print("[" + str(town.houses.index(house) + 1) + "] " + house)
            print("=====\n" +
                  str(town.numHouses) + " " + str(len(town.streets)))
            for street in town.streets:
                print(str(town.houses.index(street.house1) + 1) + " " + str(
                    town.houses.index(street.house2) + 1) + " " + str(street.cost))


"""Reads town data from file line by line. Splits line into cost, house1, and house2 to be stored as streets in town 
data """


def readTown(town, file):
    global standardFormat
    town.townReset()
    houses = []
    file = open(file, "r")
    top = file.readline().replace("\n", "")
    if top[:5] == "Town:" or top[:5] == "Name:":  # If the town file is in alternate format
        standardFormat = False
        town.name = top[6:].replace('\n', '')
        secondLine = file.readline().replace('\n', '').split(": ")
        numHouses = int(secondLine[1])
        town.numHouses = numHouses
        houses = []
        for line in file:
            if not ('=') in line:
                house = line[4:].replace('\n', '')
                houses.append(house)
            else:
                break
        numStreets = int(file.readline().replace('\n', '').split(" ")[1])
        for line in file:
            if not line:
                break
            streetLine = line.replace('\n', '').split(" ")
            street = Street(int(streetLine[2]), houses[int(streetLine[0]) - 1], houses[int(streetLine[1]) - 1])
            town.streets.append(street)
        town.houses = houses

    else:  # If the town is in standard format
        standardFormat = True
        town.name = top
        for line in file:
            if not line:
                break
            var = re.split('; |,|\*|\n', line)

            street = Street(int(var[0]), var[1].replace('"', ""), var[2].replace('"', ""))
            town.streets.append(street)
            if street.house1 not in houses:
                houses.append(street.house1)
            if street.house2 not in houses:
                houses.append(street.house2)
            town.houses = houses
            town.numHouses = len(houses)
    return town


"""
For each line in file, print the houses and find the correlating cost for the street to add up the total cost. O(s)
"""


def printPavingPlan(plan, town):
    totalCost = 0
    print(plan[0].rstrip("\n"))
    for line in plan[1:]:
        var = re.split('; |,|\*|\n', line)
        house1 = var[0].replace("\"", "")
        house2 = var[1].replace("\"", "")
        print("\"" + house1 + "\"" + "," + "\"" + house2 + "\"")
        for street in town.streets:
            if (house1 == street.house1 and house2 == street.house2) or (
                    house1 == street.house2 and house2 == street.house1):
                totalCost += street.cost
    print("Total cost = " + str(totalCost))


"""Similar to readTown. Reads paving plan file line by line and prints streets w/o cost. 
If called by checkPavingPlan, then return streets, house names, and plan cost"""


def readPavingPlan(town, file, readForCheck=False):
    planStreets = []
    planHouses = []
    plan = []
    totalCost = 0
    file = open(file, "r")
    planName = file.readline().replace("\n", "")
    plan.append(planName)

    for line in file:
        if not line or line == '\n':
            break
        var = re.split('; |,|\*|\n', line)
        house1 = var[0].replace("\"", "")
        house2 = var[1].replace("\"", "")
        plan.append("\"" + house1 + "\"" + "," + "\"" + house2 + "\"")

        if house1 not in planHouses:
            planHouses.append(house1)
        if house2 not in planHouses:
            planHouses.append(house2)
        for street in town.streets:
            if (house1 == street.house1 and house2 == street.house2) or (
                    house1 == street.house2 and house2 == street.house1):
                planStreets.append(Street(street.cost, house1, house2))
                totalCost += street.cost
                break
        if (len(planStreets)) == 0:
            print("Town data not stored to compare paving plan to."
                  "\nPlease upload town data that coincides with paving plan")
            if readForCheck:
                return None, None
            else:
                return
    if readForCheck:
        if len(planHouses) != 0 and len(planStreets) != 0:
            print(town.name.replace("\"", "") + " " + planName.replace("\"", "") + "\nTotal cost = " + str(totalCost))
        return planStreets, planHouses, totalCost
    return plan


"""
Reads current plan stored from file.
"""


def readCurrentPlan(plan, town):
    totalCost = 0
    planName = str(plan[0]).replace("\n", "")
    for p in plan:
        var = re.split('; |,|\*|\n', p)
        if planName in var:
            pass
        house1 = var[0].replace('"', "")
        house2 = var[1].replace('"', "")
        if town.numHouses != 0:
            print(house1 + ", " + house2)
            for street in town.streets:
                if house1 == street.house1 and house2 == street.house2:
                    totalCost += street.cost
                    break
        else:
            print("Town data not stored to compare paving plan to."
                  "\nPlease upload town data that coincides with paving plan")
            return

    print("Total cost of " + planName + ": " + str(totalCost))


"""Utilizes readPavingPlan() to get cost and plan data. Then passes plan data to Prim's for coverage check which is followed by a min cost check"""


def checkPavingPlan(town, file):
    townHouses = []
    for house in town.houses:
        townHouses.append([house, False])
    planStreets, planHouses, planCost = readPavingPlan(town, file, True)
    if len(planHouses) != 0 and len(planStreets) != 0:
        from Graph import Graph
        planGraph = Graph(len(planHouses))
        for street in planStreets:
            planGraph.addEdge(street.house1, street.house2, street.cost, planHouses)
        connected = planGraph.primTree(len(planHouses), planHouses, file, townHouses, True)
        if minimumCost is None:
            print(
                "The minimum cost paving plan has yet to be determined,\n"
                "please run optimal cost paving plan to find minimum cost for comparison")
        elif not connected:
            print("Optimal = NA - graph not connected")
        elif planCost == minimumCost:
            print("Optimal = yes")
        else:
            print("Optimal = no")
    else:
        print("Paving plan does not coincide with Town data")


"""Generates town data by creating a random number of houses with random names and paving costs to neighbor houses. 
Returns new Town """


def generateTown():
    roadType = ["St", "Ct", "Ave", "Ln", "Dr", "Way"]
    houseNames = open("houseNames.txt").read().splitlines()
    town = Town()
    town.name = random.choice(houseNames).capitalize().replace(" ", "") + " Town"
    randomNumbers = []
    houses = []

    # Populate random number list with random numbers
    for i in range(100):
        num = randomNumber()
        randomNumbers.append(num)

    # Utilized random int just to make sure that a town of 1 or 2 wasn't created
    numberOfHouses = random.randint(10, 50)
    town.numHouses = numberOfHouses

    for i in range(town.numHouses):
        name = str(random.randint(1, 9999)) + " " + random.choice(houseNames).capitalize() + " " + random.choice(
            roadType)
        town.houses.append(name)
        houses.append(House(name))

    for i in houses:
        passThrough = False
        while i.availableNeighbors != 0 and passThrough is False:
            # best case
            for j in houses:
                if i.name == j.name:
                    pass
                elif i.availableNeighbors == 0:
                    break
                elif not j.connected:
                    i.addNeighbor(j.name)
                    j.addNeighbor(i.name)
                    street = Street(random.choice(randomNumbers), i.name, j.name)
                    town.streets.append(street)
            # If all houses have been connected but
            for j in houses:
                if i.name == j.name:
                    pass
                elif i.availableNeighbors == 0:
                    break
                elif j.availableNeighbors != 0 and i.name not in j.neighbors:
                    i.addNeighbor(j.name)
                    j.addNeighbor(i.name)
                    street = Street(random.choice(randomNumbers), i.name, j.name)
                    town.streets.append(street)
            passThrough = True

    return town
