from sys import maxsize
INT_MAX = maxsize

'''
This returns true if either u or v is in the MST and the other is not. i.e. Has one house been paved to while 
the other is not connected.
'''
def isValidEdge(u, v, inMST):
    if u == v:
        return False
    if inMST[u] == False and inMST[v] == False:
        return False
    elif inMST[u] == True and inMST[v] == True:
        return False
    return True

class Graph():

    def __init__(self, houses):
        self.houses = houses
        self.graph = [[INT_MAX for column in range(houses)]
                      for row in range(houses)]

    def addEdge(self, v1, v2, e, vertices):
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        self.graph[index1][index2] = e
        self.graph[index2][index1] = e

    def primMST(self, numHouses, houseNames):
        pavePlan = ["MT Plan A"]
        inMST = [False] * numHouses
        # Include first vertex in MST
        inMST[0] = True

        # Keep adding edges while number of included edges does not become numHouses-1.
        edge_count = 0
        mincost = 0
        while edge_count < numHouses - 1:

            # Find minimum cost edge.
            minimumCost = INT_MAX
            a = -1
            b = -1
            for i in range(numHouses):
                for j in range(numHouses):
                    if self.graph[i][j] < minimumCost and \
                            isValidEdge(i, j, inMST):
                        minimumCost = self.graph[i][j]
                        a = i
                        b = j

            if a != -1 and b != -1:
                pavePlan.append('"' + houseNames[a] + '"' + ", " + '"' + houseNames[b] + '"')
                print("Edge %d: (%s, %s) cost: %d" %
                      (edge_count, houseNames[a], houseNames[b], minimumCost))
                edge_count += 1
                mincost += minimumCost
                inMST[b] = inMST[a] = True

        print("Minimum cost = %d" % mincost)
        return pavePlan

