from Graph import Graph
from Town import Town
import townManager
import sys
import getopt

version = "1.0"
student = "Alex Emch"

town = Town()
townManager.readTown(town, "MiniTown.txt")
currentPavingPlan = []

if __name__ == '__main__':
    if len(sys.argv) < 2:
        townManager.printTown(town)
        fileName = "planZ.txt"
        graph = Graph(town.numHouses)
        graph.createGraph(town.houses, town.streets)
        graph.primTree(town.numHouses, town.houses, fileName)

    else:
        argv = sys.argv[1:]
        opts = []
        try:
            opts, args = getopt.gnu_getopt(argv, "csar:w:e:p:zx:hu:q:v")

        except:
            print("Did not understand argument")

        for opt, arg in opts:
            match opt:
                case '-c':  # Generate random town and make it current
                    town = townManager.generateTown()
                case '-s':  # Display town in standard format
                    townManager.printTown(town)
                case '-a':  # Display town in alternate format
                    townManager.printTown(town, 2)
                case '-z':  # Display current paving plan stored
                    if not currentPavingPlan:
                        print("No current paving plan uploaded")
                    else:
                        townManager.printPavingPlan(currentPavingPlan, town)
                case '-r':  # Replace current town with data read from towndatafile
                    fileName = arg
                    townManager.readTown(town, fileName)
                case '-w':  # Write current town data to file towndatafile using the current format
                    fileName = arg
                    townManager.writeTown(town, fileName)
                case '-q':  # Write current town data to file towndatafile using the alternate format
                    fileName = arg
                    townManager.standardFormat = False
                    townManager.writeTown(town, fileName)
                case '-e':  # Read and evaluate a paving plan for the current town from file pavingplanfile
                    fileName = arg
                    currentPavingPlan = townManager.readPavingPlan(town, fileName)
                    townManager.checkPavingPlan(town, fileName)
                case '-x':  # Read a paving plan from pavingplanfile and store
                    fileName = arg
                    currentPavingPlan = townManager.readPavingPlan(town, fileName)
                case '-u':  # Write current paving plan to file pavingplanfile
                    fileName = arg
                    townManager.writePavingPlan(fileName, currentPavingPlan[0], currentPavingPlan)
                case '-p':  # Write an optimal cost paving plan for the current town to file pavingplanfile
                    fileName = arg
                    graph = Graph(town.numHouses)
                    graph.createGraph(town.houses, town.streets)
                    graph.primTree(town.numHouses, town.houses, fileName)
                case '-v':
                    print("Version: " + version + ", Student: " + student)
                case '-h':  # Show help
                    print("Syntax: Python processtown.py [-option [parameter]]\n")
                    print("  options:\n")
                    print("       c   Generate random town and make it current\n")
                    print("       s   Display town in standard format\n")
                    print("       a   Display town in alternate format\n")
                    print("       z   Display current paving plan stored\n")
                    print("       r   Replace current town with data read from towndatafile\n")
                    print("       w   Write current town data to file towndatafile using the standard format\n")
                    print("       q   Write current town data to file towndatafile using the alternate format\n")
                    print("       e   Read and evaluate a paving plan for the current town from file pavingplanfile\n")
                    print("       x   Read a paving plan from pavingplanfile and store\n")
                    print("       u   Write currently stored paving plan to file pavingplanfile\n")
                    print("       p   Write an optimal cost paving plan for the current town to file pavingplanfile\n")
                    print("       v   show version and student\n")
                    print("       h   help (this display)\n")
    exit(0)
