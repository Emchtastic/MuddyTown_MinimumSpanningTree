from sys import maxsize
import townManager

maxPlaceholder = maxsize

'''
This returns true if either u or v is in the MST and the other is not. i.e. Has one house been paved to while 
the other is not connected.
'''
def validEdge(u, v, inMST):
    if u == v:
        return False
    if inMST[u] == False and inMST[v] == False:
        return False
    elif inMST[u] == True and inMST[v] == True:
        return False
    return True

"""
Graph adjacency matrix that holds all the paving costs for connected houses
"""
class Graph():

    def __init__(self, houses):
        self.houses = houses
        self.graph = [[maxPlaceholder for column in range(houses)]
                      for row in range(houses)]

    def createGraph(self, houses, streets):
        for street in streets:
            self.addEdge(street.house1, street.house2, street.weight, houses)

    def addEdge(self, v1, v2, e, vertices):
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        self.graph[index1][index2] = e
        self.graph[index2][index1] = e

    """
    Method to determine the minimum cost to pave to every house in a town. Utilizes Prim's algorithm for greedy traversal through the adjacency matrix
    """
    def primTree(self, numHouses, houseNames, townHouses=[], checkPlan=False):
        if checkPlan:
            pavedHouses = townHouses
        pavePlan = []
        connectedTree = [False] * numHouses
        # Start with first house in connectedTree
        connectedTree[0] = True

        # Add edges while greater than numHouses-1.
        edges = 0
        planMinCost = 0
        while edges < numHouses - 1:
            minimumCost = maxPlaceholder
            a = -1
            b = -1
            for i in range(numHouses):
                for j in range(numHouses):
                    if self.graph[i][j] < minimumCost and \
                            validEdge(i, j, connectedTree):
                        minimumCost = self.graph[i][j]
                        a = i
                        b = j

            if a != -1 and b != -1:
                pavePlan.append('"' + houseNames[a] + '"' + ", " + '"' + houseNames[b] + '"')
                if not checkPlan:
                    print("%s, %s" %
                          (houseNames[a], houseNames[b]))
                edges += 1
                planMinCost += minimumCost
                connectedTree[b] = connectedTree[a] = True
                if checkPlan:
                    for house in pavedHouses:
                        if house[0] == houseNames[a] or house[0] == houseNames[b]:
                            house[1] = True

        if checkPlan:
            for house in pavedHouses:
                if house[1] == False:
                    print("This plan DOES NOT cover all houses")
                    return
            print("This plan DOES cover all houses")

        else:
            print("Minimum cost = %d" % planMinCost)
            townManager.minimumCost = planMinCost
            writeInput = input("Would you like to write this plan to file? (y/n)")
            if writeInput == 'y':
                townManager.writePavingPlan(pavePlan, True)


