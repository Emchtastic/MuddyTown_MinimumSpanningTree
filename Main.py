from Graph import Graph
from Town import Town
import townManager
import sys

town = Town()

if __name__ == '__main__':
    print(sys.version)
    print("Welcome to the MuddyTown manager")
    repeat = 'y'
    while repeat == 'y':
        answer = int(input("Enter the option (number) that you want to execute:\n"
                           "1: Generate new town\n"
                           "2: Read town from a file to store internally\n"
                           "3: Write stored town data to file\n"
                           "4: Display stored town data\n"
                           "5: Read a paving plan from file\n"
                           "6: Write paving plan to file\n"
                           "7: Check if a paving plan satisfies paving coverage and meets the minimum paving cost\n"
                           "8: Create a minimum cost paving plan for the currently store town\n"
                           "9: Compare random number generators"))

        match answer:
            case 1:
                town = townManager.generateTown()
            case 2:
                town = townManager.readTown(town)
            case 3:
                townManager.writeTown(town)
            case 4:
                townManager.printTown(town)
            case 5:
                townManager.readPavingPlan(town)
            case 6:
                townManager.writePavingPlan()
            case 7:
                townManager.checkPavingPlan(town)
            case 8:
                graph = Graph(town.numHouses)
                graph.createGraph(town.houses, town.streets)
                graph.primTree(town.numHouses, town.houses)
            case 9:
                townManager.compareNumGenerators()

        repeat = input("Would you like to return to the menu? (y/n)")

    print("Goodbye!")
