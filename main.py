from map import Map_Obj
from aStar import aStar
from util import animateAStar

# Init task
task = Map_Obj(2)

# Define start and end nodes
startNode = (task.get_start_pos()[0], task.get_start_pos()[1])
endNode = (task.get_goal_pos()[0], task.get_goal_pos()[1])

# Find shortest path
path, closedList = aStar(task)

# Animate shortest path on the map
animateAStar(task.int_map, path, closedList, startNode, endNode)