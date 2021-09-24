from map import Map_Obj
from aStar import aStar
from util import animateAStar
# from pprint import pprint


task = Map_Obj(3)

path = aStar(task)

animateAStar(path, task.int_map)