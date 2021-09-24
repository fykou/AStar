from map import Map_Obj
from aStar import aStar
from util import animateAStar


task = Map_Obj(3)

path = aStar(task)

animateAStar(task.int_map, path)