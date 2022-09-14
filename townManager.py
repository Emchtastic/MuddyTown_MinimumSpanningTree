
import Street, Town, House, random

town = Town.Town("", 0)
s=0

def randomNumber():
    a = 11
    c = 17
    m = 25
    global s

    s = (a * s + c) % m
    
    return s


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

        street = Street.Street(var[0], var[1], var[2])
        town.streets.append(street)


def generateTown():
    streetNames = [str]
    randomNumbers = [int]
    file = open("names.txt", "r")
    for line in file:
        streetNames.append(line)
    
    for i in range(100):
        num = randomNumber()
        randomNumbers.append(num)

    

if __name__ == '__main__':
    createFile("test.txt")
    readFile("test.txt")

    print(town.name)
    for street in town.streets:
        print(street.weight)
        print(street.house1 + " " + street.house2)
        generateTown()

