import random, re
from Town import Town
from Street import Street
from House import House



town = Town("", 0)
s = 0

def randomNumber():
    a = 32
    c = 12
    m = 43
    global s

    s = (a * s + c) % m

    return s


def createFile(name):
    file = open(name, "w")
    file.write("Hobbsville\n")
    for street in town.streets:
        file.write(str(street.weight) + ', "' + street.house1 + '",' + ' "' + street.house2 + '"\n')


def readFile(name):
    file = open(name, "r")
    town.name = file.readline()
    for line in file:
        if not line:
            break
        var = re.split('; |, |\*|\n', line)

        street = Street.Street(var[0], var[1].replace('"', ""), var[2].replace('"', ""))
        town.streets.append(street)




def generateTown():
    randomNumbers = []
    houses = []
    roadType = ["St", "Ct", "Ave", "Ln", "Dr", "Way"]
    streetNames = open("names.txt").read().splitlines()

    for i in range(100):
        num = randomNumber()
        randomNumbers.append(num)

    numberOfHouses = 6  # random.choice(randomNumbers)

    for i in range(numberOfHouses):
        name = str(random.randint(1, 9999)) + " " + random.choice(streetNames).capitalize() + " " + random.choice(roadType)
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
                    print("first loop add")
                    i.addNeighbor(j.name)
                    j.addNeighbor(i.name)
                    street = Street(randomNumber(), i.name, j.name)
                    town.streets.append(street)
            # If all houses have been connected but
            """
            for j in houses:
                if i.name == j.name:
                    pass
                elif i.availableNeighbors == 0 :
                    break
                elif j.availableNeighbors != 0 and i.name not in j.neighbors:
                    print("Second loop add")
                    i.addNeighbor(j.name)
                    j.addNeighbor(i.name)
                    street = Street(randomNumber(), i.name, j.name)
                    town.streets.append(street)
            """
            passThrough = True

    return town


if __name__ == '__main__':
    generateTown()
    createFile("test.txt")

    print(town.name)
    for street in town.streets:
        print(str(street.weight) + " " + street.house1 + " " + street.house2)
