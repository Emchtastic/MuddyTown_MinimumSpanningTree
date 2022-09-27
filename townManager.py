import random, re
import time

from Street import Street
from House import House
from Town import Town

minimumCost = None
s = 0

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


"""Street values from passed town object are written to file"""


def writeTown(town):
    file = open(input("Enter a name for the file to be written to"), "w")
    file.write(town.name + "\n")
    for street in town.streets:
        file.write(str(street.weight) + ', "' + street.house1 + '",' + ' "' + street.house2 + '"\n')


"""
If the paving plan is coming from Prim's, write the passed street values to write. Else, write user input to file.
"""


def writePavingPlan(pavingPlan=[], isMST=False):
    file = open(input("Enter the name of the file to write to: "), "w")
    file.write(input("Enter the name of the paving plan") + "\n")
    if isMST:
        for street in pavingPlan:
            file.write(street + "\n")
    else:
        yes = 'y'
        while yes == 'y':
            house1 = str(input("Enter the name of the first house"))
            house2 = str(input("Enter the name of the second house"))
            file.write('"' + house1 + '", ' + '"' + house2 + '"\n')

            yes = input("Add another street? (y/n)")

def printTown(town):
    print(town.name)
    for street in town.streets:
        print(str(street.weight) + ", " + street.house1 + ", " + street.house2)


"""Reads town data from file line by line. Splits line into cost, house1, and house2 to be stored as streets in town data"""


def readTown(town):
    town.townReset()
    houses = []
    file = open(input("Enter name of town file to read: "), "r")
    town.name = file.readline().replace("\n", "")
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
    print(town.name + " has been uploaded and stored")
    return town


"""Similar to readTown. Reads paving plan file line by line and prints streets w/o cost. 
If called by checkPavingPlan, then return streets, house names, and plan cost"""


def readPavingPlan(town, readForCheck=False):
    planStreets = []
    planHouses = []
    plan = []
    totalCost = 0
    filename = input("Enter file name with paving plan")
    file = open(filename, "r")
    planName = file.readline()
    plan.append(planName)
    print("Reading paving plan titled: " + planName.rstrip("\n"))

    for line in file:
        if not line:
            break
        var = re.split('; |, |\*|\n', line)
        house1 = var[0].replace('"', "")
        house2 = var[1].replace('"', "")
        plan.append(house1+", "+house2)
        if town.numHouses != 0:
            print(house1 + ", " + house2)

            if house1 not in planHouses:
                planHouses.append(house1)
            if house2 not in planHouses:
                planHouses.append(house2)
            for street in town.streets:
                if house1 == street.house1 and house2 == street.house2:
                    planStreets.append(Street(street.weight, house1, house2))
                    totalCost += street.weight
                    break
        else:
            print("Town data not stored to compare paving plan to."
                  "\nPlease upload town data that coincides with paving plan")
            if readForCheck:
                return None, None
            else:
                return
    print("Total cost of stored plan: " + str(totalCost))
    if readForCheck:
        return planStreets, planHouses, totalCost
    return plan


def readCurrentPlan(plan, town):
    totalCost = 0
    planName = str(plan[0]).replace("\n", "")
    for street in plan:
        var = re.split('; |, |\*|\n', street)
        if planName in var:
            pass
        house1 = var[0].replace('"', "")
        house2 = var[1].replace('"', "")
        if town.numHouses != 0:
            print(house1 + ", " + house2)
            for street in town.streets:
                if house1 == street.house1 and house2 == street.house2:
                    totalCost += street.weight
                    break
        else:
            print("Town data not stored to compare paving plan to."
                  "\nPlease upload town data that coincides with paving plan")
            return

    print("Total cost of " + planName + ": " + str(totalCost))



"""Utilizes readPavingPlan() to get cost and plan data. Then passes plan data to Prim's for coverage check which is followed by a min cost check"""


def checkPavingPlan(town):
    townHouses = []
    for house in town.houses:
        townHouses.append([house, False])
    planStreets, planHouses, planCost = readPavingPlan(town, True)
    if planHouses is not None and planStreets is not None:
        from Graph import Graph
        planGraph = Graph(len(planHouses))
        for street in planStreets:
            planGraph.addEdge(street.house1, street.house2, street.weight, planHouses)
        planGraph.primTree(len(planHouses), planHouses, townHouses, True)
        if minimumCost is None:
            print(
                "The minimum cost paving plan has yet to be determined,\n please run option 8 to find minimum cost for comparison")
        elif planCost == minimumCost:
            print("This plan achieves the minimum cost to pave to each house")
        else:
            print("This plan DOES NOT achieve the minimum cost to pave to each house")


"""Generates town data by creating a random number of houses with random names and paving costs to neighbor houses. 
Returns new Town """


def generateTown():
    town = Town()
    town.name = input("Please enter a name for the new town")
    randomNumbers = []
    houses = []
    roadType = ["St", "Ct", "Ave", "Ln", "Dr", "Way"]
    houseNames = open("houseNames.txt").read().splitlines()

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

    print(town.name + " has been created")
    return town
