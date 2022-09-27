Course: CS 4050 Algorithms and Algorithm Analysis Fall 2022
Student: Alex Emch
Project: Muddy Town

Scope: This program writes/reads town and paving data to be analyzed for connectivity, paving coverage, and paving cost

How to use:
Main.py - This class is the driver for the program. There is a menu to choose options that address each objective for
the project. A Town object is instantiated here and passed to methods within townManager.py and Graph.py

Python Classes:
-Town.py: This is an object class used to construct town objects. This object keeps track of the streets in the town as well as house names
    and the number of houses in the town
-Street.py: This is an object class used to construct street objects. These street objects are used to store house names and costs
    for the streets to pave
-House.py: This is an object class used to construct house objects. These objects are utilized when generating a town from
    scratch and determining which houses are adjacent to each other
-Graph.py: Responsible for creating and housing the adjacency matrix which holds the paving costs between houses. Also
    contains a modified Prim's algorithm to determine the minimum cost paving plan and if a paving plan paves to
    all of a town's houses
-townManager.py: This class manages all the I/O for town and paving plan files. It also holds the algorithms that print and verify paving plans.
    This class also contains the pseudo-random number generator and the method to compare to Python's RNG

Other files:
-houseNames.txt: A large list of random street names that this program utilizes to randomly create house names