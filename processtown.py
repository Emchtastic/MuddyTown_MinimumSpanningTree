from Graph import Graph
from Town import Town
import townManager
import sys
import getopt

town = Town()
townManager.readTown(town, "MiniTown.txt")
currentPavingPlan = []

if __name__ == '__main__':
    if len(sys.argv) < 2:
        townManager.printTown(town)
        fileName = "PlanZ.txt"
        graph = Graph(town.numHouses)
        graph.createGraph(town.houses, town.streets)
        graph.primTree(town.numHouses, town.houses, fileName)
        currentPavingPlan = townManager.readPavingPlan(town, fileName)
        townManager.writePavingPlan("newPlan.txt", currentPavingPlan[0], currentPavingPlan)
        townManager.printPavingPlan(currentPavingPlan, town)
        townManager.checkPavingPlan(town, "planB.txt")
    else:
        argv = sys.argv[1:]
        try:
            opts, args = getopt.gnu_getopt(argv, "csar:w:e:p:zx:hu:")

        except:
            print("Error")

        for opt, arg in opts:
            match opt:
                case '-c':                              # Generate random town
                    town = townManager.generateTown()
                case '-s':                              # Display town in standard format
                    townManager.printTown(town)
                case '-a':                              # Display town in alternate format
                    townManager.printTown(town, 2)
                case '-z':                              # Display current paving plan stored
                    if not currentPavingPlan:
                        print("No current paving plan uploaded")
                    else:
                        townManager.printPavingPlan(currentPavingPlan, town)
                case '-r':                              # Replace current town with data read from file
                    fileName = arg
                    townManager.readTown(town, fileName)
                case '-w':                              # Write current town data to file towndatafile using the standard format
                    fileName = arg
                    townManager.writeTown(town, fileName)
                case '-e':                              # Read and evaluate a paving plan for the current town from file pavingplanfile
                    fileName = arg
                    townManager.checkPavingPlan(town, fileName)
                case '-x':                              # Read a paving plan from file and store
                    fileName = arg
                    currentPavingPlan = townManager.readPavingPlan(town, fileName)
                case '-u':                              # Write current paving plan to file pavingplanfile
                    fileName = arg
                    townManager.writePavingPlan(fileName, currentPavingPlan[0], currentPavingPlan)
                case '-p':                              # Write an optimal cost paving plan for the current town to file pavingplanfile
                    fileName = arg
                    graph = Graph(town.numHouses)
                    graph.createGraph(town.houses, town.streets)
                    graph.primTree(town.numHouses, town.houses, fileName)
                case '-h':                              # Show help
                    print("Syntax: [-option [parameter]]\n")
                    print("  options:\n")
                    print("       s   show current town in standard format\n")
                    print("       a   show current town in alternate format\n")
                    print("       r   read town data from file identified by parameter\n")
                    print("       w   write current town to file identified by parameter\n")
                    print("       c   create new random town and store\n")
                    print("       w   write current town to file identified by parameter\n")
                    print("       v   show version\n")
                    print("       h   help (this display)\n")

    """
    print("Welcome to the MuddyTown manager")
    repeat = 'y'
    while repeat == 'y':
        answer = int(input("Enter the option (number) that you want to execute:\n"
                           "1: Generate new town\n"#
                           "2: Read town from a file to store internally\n"#
                           "3: Write stored town data to file\n"#
                           "4: Display stored town data\n"#
                           "5: Read a paving plan from file\n"#
                           "6: Display currently stored paving plan\n"#
                           "7: Write paving plan to file\n"
                           "8: Check if a paving plan satisfies paving coverage and meets the minimum paving cost\n"
                           "9: Create a minimum cost paving plan for the currently store town\n"
                           "10: Compare random number generators"))

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
                currentPavingPlan = townManager.readPavingPlan(town)
            case 6:
                townManager.readCurrentPlan(currentPavingPlan, town)
            case 7:
                townManager.writePavingPlan()
            case 8:
                townManager.checkPavingPlan(town)
            case 9:
                graph = Graph(town.numHouses)
                graph.createGraph(town.houses, town.streets)
                graph.primTree(town.numHouses, town.houses)
            case 10:
                townManager.compareNumGenerators()

        repeat = input("Would you like to return to the menu? (y/n)")

    """
