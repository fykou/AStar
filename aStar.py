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

    openList.put(startNode)

    while not openList.empty():
        currentNode = openList.get()  # TODO: prioritize Node.f
        print(currentNode)

        # At end
        if currentNode == goalNode:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.pos)
                current = current.parent
            return path[::-1] # Return reversed path



    return
