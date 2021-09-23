from queue import PriorityQueue

from map import Map_Obj
from util import Node


def aStar(task):
    # Init start node
    startNode = Node(None, tuple(task.get_start_pos()))
    startNode.h = startNode.g = startNode.f = 0

    # Init goal node
    goalNode = Node(None, tuple(task.get_goal_pos()))
    goalNode.h = goalNode.g = goalNode.f = 0

    openList = PriorityQueue()
    closedList = []

    openList.put(startNode)

    while not openList.empty():
        currentNode = openList.get()  # TODO: prioritize Node.f
        closedList.append(currentNode)

        # At end
        if currentNode.pos == goalNode.pos:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.pos)
                current = current.parent
            return path[::-1] # Return reversed path

        children = []

        for movePos in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            newPos = currentNode.pos[0] + movePos[0], currentNode.pos[1] + movePos[1]

            if task.get_cell_value(newPos) == -1: # Wall
                continue
                
            newNode = Node(currentNode, newPos)

            children.append(newNode)

            # Loop through children
        for child in children:

            # Child is on the closed list
            #TODO: optimize
            if (child in closedList or True in map(lambda x: child.pos == x.pos, (elem for elem in list(openList.queue)))) and (currentNode.g + 1 > child.g) :
                    continue


            child.g = currentNode.g + 1
            child.h = ((child.pos[0] - goalNode.pos[0]) ** 2) + ((child.pos[1] - goalNode.pos[1]) ** 2)
            child.f = child.g + child.h
            child.parent = currentNode

            print(child)

            openList.put(child)
