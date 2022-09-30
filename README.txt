Course: CS 4050 Algorithms and Algorithm Analysis Fall 2022
Student: Alex Emch
Project: Muddy Town
Program Language/Version: Python 3.10 - needed for match-case statements

Scope: This program writes/reads town and paving data to be analyzed for connectivity, paving coverage, and paving cost

How to use:
processtown.py - This class is the driver for the program. This class utlizies getopt().gnu_getopt commands for Python
Syntax: Python processtown.py [-option [parameter]]
options:
    -c                      Generate random town and make it current
    -s                      Display town in standard format
    -a                      Display town in alternate format
    -z                      Display current paving plan stored
    -r [towndatafile]       Replace current town with data read from towndatafile
    -w [towndatafile]       Write current town data to file towndatafile using the standard format
    -q [towndatafile]       Write current town data to file towndatafile using the alternate format
    -e [pavingplanfile]     Read and evaluate a paving plan for the current town from file pavingplanfile
    -x [pavingplanfile]     Read a paving plan from pavingplanfile and store
    -u [pavingplanfile]     Write currently stored paving plan to file pavingplanfile
    -p [pavingplanfile]     Write an optimal cost paving plan for the current town to file pavingplanfile
    -v                      show version and student
    -h                      help

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
-MiniTown.txt: test case/default town