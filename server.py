"""
Akshay Mohabey
Python 3.12.4
Mac OSX
11 July 2024

Lethal Theory
Sever/Vizualization File
""" 
# Importing Dependencies
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule
from mesa.visualization.UserParam import Slider

#Import model
from model import LethalModel
import parameters as p
import agents


# Color Scheme 2
citizen_color = "#3b7a57"
militant_color = "#fff600"
msquad_color = "#cc5500"

def agent_portrayal(agent):
    portrayal = {
      "Shape": "circle",
      "Filled": True}
    if agent.identity == '0':
      portrayal["r"] = 0.50
      portrayal["Color"] = citizen_color
      portrayal["Layer"] = 0
    elif agent.identity == '1':
      portrayal["r"] = 0.35
      portrayal["Color"] = militant_color
      portrayal["Layer"] = 1
    else:
      portrayal["r"] = 0.30
      portrayal["Color"] = msquad_color
      portrayal["Layer"] = 2
    return portrayal

grid = CanvasGrid(
  agent_portrayal,
  p.grid_x,
  p.grid_y,
  500,
  500)

chart = ChartModule(
  [{'Label': "citizens",'Color': '#3b7a57'},{'Label': "militants",'Color': '#fff600'},{'Label': "msqad",'Color': '#cc5500'}],
  data_collector_name='datacollector'
  )

# Generating Slider
# militants_slider = Slider("Number of Militants", value=20, min_value=12, max_value=30, step=1)
# msquad_slider = Slider("Number of Military Squads", value=7, min_value=2, max_value=10, step=1)

# server = ModularServer(
#   LethalModel,
#   [grid, chart],
#   "Lethal Theory",
#   {"citizens":p.No_of_Citizens,
#    "militants": militants_slider,
#    "military_squad":msquad_slider}
#   )
server = ModularServer(
  LethalModel,
  [grid, chart],
  "Lethal Theory",
  {"citizens":p.No_of_Citizens,
   "militants": p.No_of_Militants,
   "military_squad":p.No_of_MilitarySquad}
  )
server.port = 8521 # Any non-80 port to appease replit
server.launch()