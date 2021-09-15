from map import Map_Obj
from aStar import aStar
from util import Node
from pprint import pprint


task1 = Map_Obj(1)

map_int, map_str = task1.get_maps()

# task1.print_map(map_int) #Prints map in terminal
# task1.show_map() #Shows map in PIL


startNode = Node(None, tuple(task1.get_start_pos()))
goalNode = Node(None, tuple(task1.get_goal_pos()))

colums = len(map_int)
rows = len(map_int[0])

nodes = []

for i in range(colums-1):
    for j in range(rows-1):
        if task1.get_cell_value([i,j]) == 1:
            nodes.append(Node(None, tuple([i, j])))
    


pprint(nodes)


# print(startNode.getPos())
