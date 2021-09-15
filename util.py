
from enum import Enum

class State(Enum):
    OPEN = 'Open'
    CLOSED = 'Closed'

    
class Node:
    def __init__(self, status:State, pos=None, parent=None):
        self.pos = pos #task.get_cell_value([x, y])
        self.status = status # open, closed
        self.parent = parent
        self.h = 0 # heuristic cost to goal
        self.g = 0 # cost to node
        self.f = 0 # h + g
    
    def __repr__(self):
        return f"{self.pos}"

    def getPos(self):
        return self.pos

    
