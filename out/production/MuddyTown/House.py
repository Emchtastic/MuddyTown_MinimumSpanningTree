import random

class House:
    def __init__(self, name):
        self.name = name
        self.numNeighbors = random.randrange(2, 5)
        self.neighbors = []
        self.connected = False
        self.availableNeighbors = self.numNeighbors

    def addNeighbor(self, neighbor):
        self.connected = True
        self.neighbors.append(neighbor)
        self.availableNeighbors = self.numNeighbors - len(self.neighbors)
