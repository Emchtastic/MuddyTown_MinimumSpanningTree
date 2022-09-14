import random
class Street:
    def __init__(self, weight, house1, house2):
        self.weight = weight
        self.house1 = house1
        self.house2 = house2


class Town:
    def __init__(self, name, houses):
        self.name = name
        self.houses = houses
        self.streets = []


town = Town("", 0)


def createFile(name):
    file = open(name, "w")
    file.write("Hobbsville\n" +
               "3,1 First Street,2 First Street\n" +
               "2,1 Second Street,1 First Street\n" +
               "2,2 First Street,2 Second Street")


def readFile(name):
    file = open(name, "r")
    town.name = file.readline()
    for line in file:
        if not line:
            break
        var = line.split(',', -1)

        street = Street(var[0], var[1], var[2])
        town.streets.append(street)


def generateTown():
    return


if __name__ == '__main__':
    createFile("test.txt")
    readFile("test.txt")

    print(town.name)
    for street in town.streets:
        print(street.weight)
        generateTown()
        print(street.house1 + " " + street.house2)
