"""
Class that holds all town data which includes the name of the town, the names of the houses in the town, the streets, and the number of houses
"""


class Town:
    def __init__(self, name="", houses=None, numHouses=0):
        if houses is None:
            houses = []
        self.name = name
        self.houses = houses
        self.numHouses = numHouses
        self.streets = []

    def townReset(self):
        self.name = ""
        self.houses = []
        self.numHouses = 0
        self.streets = []