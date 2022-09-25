from Graph import Graph
import townManager

if __name__ == '__main__':
    global vertices
    global verticesNum
    town = townManager.town
    townManager.readTown("town.txt")
    graph = Graph(town.numHouses)
    for street in town.streets:
        graph.addEdge(street.house1,street.house2, street.weight, town.houses)
    townManager.readPavingPlan()
    townManager.printTown()
    graph.primMST(town.numHouses, town.houses)
