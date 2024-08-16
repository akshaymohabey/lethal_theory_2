"""
Akshay Mohabey
Python 3.12.4
Mac OSX
11 July 2024

Lethal Theory
Parameters File
"""
# Importing Dependencies
import random
import mesa

# Grid Size
grid_x = 15
grid_y = 15

# Define numeric values of Citizens, Militants, MilitarySquad
No_of_Citizens = grid_x * (grid_y-1)
#No_of_Citizens = 0
No_of_Militants = random.randint(12, 30)
#No_of_Militants = 0
No_of_MilitarySquad = random.randint(int((grid_x)/2),grid_x)
#No_of_MilitarySquad = random.randint(0,grid_x)
#No_of_MilitarySquad = 0