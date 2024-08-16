'''

Have made the below changes to the file
1. Initial position of the agents and their strength (to signify count):
    MSquad- At y=0, no overlapping of 2 agents. Strength = 7 for now.
    Militants- Randomly across the grid, except the first row. Strength = 1 for now, can make it probabilistic if required.
    Citizens- Occupying all the grids, except the first wor. Strength = rand(2,6)

2. Movement of MSquad:
    No moore movement, only horizontal or vertical
    get the neighbouring position, if there is a militant nearby, they choose those cells for the movement
    else they randomly move to other neighbouring cells without moving back to their already visited position
    global list to store the moved positions travelled by the Squad

3. Movement of Militant
    Can move diagonally as well, but no information about the neighbouring cells
    Half probability of not to move and stay at their existing position

4. Interaction of MSquad and Militants
    For now hardcoded probability of 70% to reduce the militant's strength and 30% to reduce the Squad's strength
    Can make the probability agent specific at later stages

5. Interaction of MSquad and Citizens
   For now hardcoded probability of 90% to reduce the citizen's strength and no harm to the Squad's strength
   Can make the probability agent specific at later stages

'''