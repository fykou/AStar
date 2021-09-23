from queue import PriorityQueue
from util import Node, State


def aStar(task):
    # Init start node
    startNode = Node(tuple(task.get_start_pos()))

    # Init goal node
    goalNode = Node(tuple(task.get_goal_pos()))

    openList = PriorityQueue()
    openList.put(startNode)

    while not openList.empty():
        currentNode = openList.get()
        currentNode.status = State.CLOSED

        # At end
        if currentNode.pos == goalNode.pos:
            path = []
            current = currentNode
            print(currentNode)
            while current is not None:
                path.append(current.pos)
                current = current.parent
            return path[::-1] # Return reversed path

        children = []

        for movePos in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            newPos = currentNode.pos[0] + movePos[0], currentNode.pos[1] + movePos[1]

            if task.get_cell_value(newPos) == -1: # Wall
                continue
                
            newNode = Node(newPos, currentNode)
            children.append(newNode)

        for child in children:

            if (child.status == State.CLOSED or True in map(lambda x: child.pos == x.pos, (elem for elem in list(openList.queue)))) and (currentNode.g + 1 > child.g) :
                    continue

            child.g = currentNode.g + 1
            child.h = ((child.pos[0] - goalNode.pos[0]) ** 2) + ((child.pos[1] - goalNode.pos[1]) ** 2)
            child.f = child.g + child.h
            child.parent = currentNode

            openList.put(child)
