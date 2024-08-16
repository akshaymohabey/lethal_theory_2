"""
Akshay Mohabey
Python 3.12.4
Mac OSX
11 July 2024

Lethal Theory
Run File
"""
# Importing Dependencies
from model import LethalModel
import mesa
import parameters as p
import matplotlib.pyplot as plt
import random
import seaborn as sns
import numpy as np
import pandas as pd


# Calling model class
main_instance = LethalModel(p.No_of_Citizens,p.No_of_Militants,p.No_of_MilitarySquad)

agent_counts = np.zeros((main_instance.grid.width, main_instance.grid.height))
for cell_content, (x, y) in main_instance.grid.coord_iter():
    agent_count = len(cell_content)
    agent_counts[x][y] = agent_count


# Plotting the graph using Seaborn

g = sns.heatmap(agent_counts, cmap="viridis", annot=True, cbar=False, square=True)
g.figure.set_size_inches(4, 4)
g.set(title="Number of agents on each cell of the grid");
plt.show()


# Batch Run
# params = {"citizens": p.No_of_Citizens, 
#           "militants": p.No_of_Militants,
#           "military_squad": p.No_of_MilitarySquad}

# results = mesa.batch_run(
#             LethalModel,
#             parameters = params,
#             iterations=100,
#             max_steps=100,
#             number_processes = 1,
#             data_collection_period = 1,
#             display_progress = True
#             )

# results_df = pd.DataFrame(results)
# print(results_df.keys())



