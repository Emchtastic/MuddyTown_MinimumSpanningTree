from sys import maxsize
import townManager

maxPlaceholder = maxsize

'''
This returns true if either u or v is in the MST and the other is not. i.e. To be True one house must been paved to while 
the other has not. Ensure no house islands!
'''


def validEdge(h1, h2, paved):
    if h1 == h2:
        return False
    if paved[h1] is False and paved[h2] is False:
        return False
    elif paved[h1] is True and paved[h2] is True:
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
            self.addEdge(street.house1, street.house2, street.cost, houses)

    """
    Adds cost of paving between houses to adjacency matrix
    """

    def addEdge(self, v1, v2, e, vertices):
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        self.graph[index1][index2] = e
        self.graph[index2][index1] = e

    """
    Method to determine the minimum cost to pave to every house in a town. Utilizes Prim's algorithm for greedy traversal through the adjacency matrix
    """

    def primTree(self, numHouses, houseNames, planFileName, townHouses=[], checkPlan=False):
        if checkPlan:
            pavedHouses = townHouses
        pavePlan = []
        pavePlan.append(str(planFileName).replace(".txt", ""))
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
                pavePlan.append('"' + houseNames[a] + '"' + "," + '"' + houseNames[b] + '"')
                edges += 1
                planMinCost += minimumCost
                connectedTree[b] = connectedTree[a] = True
                if checkPlan:
                    for house in pavedHouses:
                        if house[0] == houseNames[a] or house[0] == houseNames[b]:
                            house[1] = True

        if checkPlan:
            for house in pavedHouses:
                if house[1] is False:
                    print("Connected = no")
                    return False
            print("Connected = yes")
            return True

        else:
            townManager.minimumCost = planMinCost
            townManager.writePavingPlan(planFileName, pavePlan[0], pavePlan)
