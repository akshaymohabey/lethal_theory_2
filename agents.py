"""
Akshay Mohabey
Python 3.12.4
Mac OSX
11 July 2024

Lethal Theory
Agents File
"""

# Importing dependencies
import mesa
import random
import networkx as nx
import parameters as p

# Citizen Class
class Citizen(mesa.Agent):
    def __init__(self,citizen_id,model):
        super().__init__(citizen_id,model)
        # print("Hello, I am Citizen:",citizen_id)
        self.identity = '0'
        self.strength = random.choice(range(4,6))
    
    def step(self):
        pass

# Militant Class 
class Militant(mesa.Agent):
    def __init__(self,militant_id,model):
        super().__init__(militant_id,model)
        # print("Hello, I am Militant:",militant_id)
        self.identity = '1'
        self.strength = 1
    
    def move(self):
            if self.pos is not None:
                # Check if a military squad is present in the current cell
                cell_contents = self.model.grid.get_cell_list_contents(self.pos)
                if any(agent.identity == '2' for agent in cell_contents):
                    return  # Do not move if a military squad is present

                possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
                possible_steps = [step for step in possible_steps if step[1] != 0]  # Avoid moving to the first row
                if possible_steps:
                    new_position = self.random.choice(possible_steps)
                    # 50% Probability to move
                    if random.random() > 0.5:
                        self.model.grid.move_agent(self, new_position)
        
    def step(self):
        self.move()

# Military Squad
moved_positions = []
class MSquad(mesa.Agent):
    def __init__(self,msquad_id,model):
        super().__init__(msquad_id,model)
        # print('Hello! this is the Military Squad',msquad_id)
        self.identity = '2'
        self.strength = 7

    def move(self):
        global moved_positions
        if self.pos != None:
            possible_steps = self.model.grid.get_neighborhood(self.pos, moore=False, include_center=False)
            possible_steps = [step for step in possible_steps
                                    if not any(agent.identity == '2' for agent in self.model.grid.get_cell_list_contents(step))
                                    ]
            # new_position = self.random.choice(possible_steps)
            # self.model.grid.move_agent(self, new_position)
            Militant_opt = []

            for pos in possible_steps:
                # Get the agents in the neighbourhood cells
                content = self.model.grid.get_cell_list_contents(pos)

                # Check for Militants
                if any(agent.identity == '1' for agent in content):
                    Militant_opt.append(pos)

            possible_steps = [step for step in possible_steps if step not in moved_positions]

            if Militant_opt:
                # Move to a random cell containing a Militant
                new_position = self.random.choice(Militant_opt)
            elif possible_steps:
                # Move to a random neighboring cell if no Militants are found
                new_position = self.random.choice(possible_steps)
            else:
                return

            # Move to the new position
            self.model.grid.move_agent(self, new_position)
            moved_positions.append(new_position)

    def interaction(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            for agent in cellmates:
                #Check for militants
                if isinstance(agent, Militant):
                    #70% probability to reduce the Militant strength
                    if random.random()<0.7:
                        agent.strength -= 1
                        if agent.strength <= 0:
                            #Remove the Militant
                            self.model.grid.remove_agent(agent)
                            self.model.schedule.remove(agent)
                    else:
                        self.strength -= 1
                        if self.strength <= 0:
                            # Remove the MSquad
                            self.model.grid.remove_agent(self)
                            self.model.schedule.remove(self)

                elif isinstance(agent, Citizen):
                    # 90% probability to reduce the Citizen strength
                    if random.random()<0.9:
                        agent.strength -= 1
                        if agent.strength <= 0:
                            # Remove the Citizen
                            self.model.grid.remove_agent(agent)
                            self.model.schedule.remove(agent)

        else:
            pass


    
    def step(self):
        self.move()
        self.interaction()