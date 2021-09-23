from map import Map_Obj
from aStar import aStar
# from pprint import pprint


task = Map_Obj(3)

path = aStar(task)


# for node in closed[1:-1]:
#     task.set_cell_value((node.pos), " ! ")

for pos in path[1:-1]:
    task.set_cell_value((pos), " @ ")

task.show_map()