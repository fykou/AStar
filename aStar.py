from queue import PriorityQueue
from util import Node

def aStar(task):
    # Init start node
    startNode = Node(None, tuple(task.get_start_pos()))
    startNode.h = startNode.g = startNode.f = 0

    # Init goal node
    goalNode = Node(None, tuple(task.get_goal_pos()))
    goalNode.h = goalNode.g = goalNode.f = 0

    openList = PriorityQueue()
    closeList = []

    openList.append(startNode)

    while len(openList > 0):
        currentNode = openList.get()  # TODO: prioritize Node.f


        # At end
        if currentNode == goalNode:
            path = []



    return
