"""
Akshay Mohabey
Python 3.12.4
Mac OSX
11 July 2024

Lethal Theory
Model File
"""
# Importing Dependencies
import mesa
import parameters as p
import networkx as nx
import agents
import copy
import random

# Returns total number of citizens in the model at a time
def total_citizens(model):
    x = 0
    for agent in model.citizens_list:
        x = x + agent.strength
    return x

# Returns total number of militants in the model at a time
def total_militants(model):
    x = 0
    for agent in model.militants_list:
        x = x + agent.strength
    return x

# Returns total number of Military squads at a time
def total_msquad(model):
    x = 0
    for agent in model.military_squads_list:
        x = x + agent.strength
    return x

# Agents killed in Warfare
def killed_citizens(model):
    return model.init_citizens - total_citizens(model)

def killed_militants(model):
    return model.init_militants - total_militants(model)

def killed_msquad(model):
    return model.init_msquad - total_msquad(model)


# Model Class
class LethalModel(mesa.Model):

    def __init__(self, citizens,militants,military_squad):
        super().__init__()
        self.num_of_citizens = citizens
        self.num_of_militants = militants
        self.num_of_msquad = military_squad

        self.citizens_list = []
        self.militants_list = []
        self.military_squads_list = []

        # Add grid
        self.grid = mesa.space.MultiGrid(p.grid_x,p.grid_y,False)

        # Create random scheduler and assign it to Model
        self.schedule = mesa.time.RandomActivation(self)
        self.running = True

        """ 
        Creating Citizens
        """
        for i in range(self.num_of_citizens):
            x = agents.Citizen(LethalModel.next_id(self),self)  
            # Adding agent to the schedule
            self.schedule.add(x)
            self.citizens_list.append(x)

        # Adding    
        ctz = 0 
        for column in range(p.grid_x):
            for row in range(p.grid_y-1):
            # Addding Militans to a random cell
                coord_x = column
                coord_y = row + 1
                self.grid.place_agent(self.citizens_list[ctz],(coord_x,coord_y))
                ctz += 1
        # Initial no. of citizens
        self.init_citizens = total_citizens(self)
        
        # Creating Militants
        for j in range(self.num_of_militants):
            y = agents.Militant(LethalModel.next_id(self),self)

            # Adding militants to te schedule 
            self.schedule.add(y)
            self.militants_list.append(y)

            # Addding Militans to a random cell
            coord_x = self.random.randrange(self.grid.width)  
            coord_y = self.random.randrange(self.grid.height-1)+1
            self.grid.place_agent(y,(coord_x,coord_y))

        self.init_militants = total_militants(self)
        
        # Creating Military Squad
        for k in range(self.num_of_msquad):
            z = agents.MSquad(LethalModel.next_id(self),self)

            #Adding Military Squad to the schedule
            self.schedule.add(z)
            self.military_squads_list.append(z)

            # Find empty cells in the first row (y = 0)
            empty_cells = [(x, 0)
                            for x in range(self.grid.width)
                                if self.grid.is_cell_empty((x, 0))]

            # Addding Militans to a random cell
            if empty_cells:
                # Place the squad in a random empty cell in the first row
                coord = self.random.choice(empty_cells)
                self.grid.place_agent(z, coord)
            else:
                pass
            
            # Self Initial Military Agents
            self.init_msquad = total_msquad(self)

        self.datacollector = mesa.DataCollector(
        model_reporters = {"citizens": killed_citizens, "militants": killed_militants, "msquad": killed_msquad}
        )

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

    # Setter and getter functions
    def get_citizens_list(self):
        return self.citizens_list
    
    def get_militatnts_list(self):
        return self.militants_list
    
    def get_msquad_list(self):
        return self.military_squads_list
        