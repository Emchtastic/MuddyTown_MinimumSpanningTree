"""
Class that holds all street data, i.e. houses and cost to pave between them
"""

class Street:
    def __init__(self, cost, house1, house2):
        self.cost = cost
        self.house1 = house1
        self.house2 = house2
