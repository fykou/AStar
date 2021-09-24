from queue import PriorityQueue


def aStar(task):
    class Node:
        def __init__(self, pos, parent=None):
            self.pos = pos  # task.get_cell_value([x, y])
            self.parent = parent
            self.h = 0  # heuristic cost to goal
            self.g = 0  # cost to node
            self.f = 0  # h + g

        def __repr__(self):
            return f"Pos: {self.pos} - Cost: {self.f} | "

        #Custom for PriorityQueue
        def __lt__(self, other):
            return self.f < other.f


    startNode = Node(tuple(task.get_start_pos())) # Init start node

    goalNode = Node(tuple(task.get_goal_pos())) # Init goal node

    # Init open and closed lists.
    openList = PriorityQueue()
    closedList = []
    openList.put(startNode)

    while not openList.empty():
        currentNode = openList.get() # Pop node from top of stack based on f value
        closedList.append(currentNode.pos) # Add node to closedList

        if currentNode.pos == goalNode.pos: # Check for finish condition
            path = []
            current = currentNode
            while current is not None:
                path.append(current.pos)
                current = current.parent # Traverse backwards through parents
            return path[::-1], closedList # Return reversed path and searched nodes


        children = []
        for movePos in [(1, 0), (-1, 0), (0, 1), (0, -1)]: # List for adjacent positions
            newPos = currentNode.pos[0] + movePos[0], currentNode.pos[1] + movePos[1] # New potential position for a node

            if task.get_cell_value(newPos) == -1: # Check if position is a wall
                continue
                
            newNode = Node(newPos, currentNode) # Create new node on that position and add parent
            children.append(newNode) # Add position to children

        for child in children:

            # Check if current child is in any of the open or closed lists, or if the g value is lower than the current node's g value.
            if (child.pos in closedList) or (True in map(lambda x: child.pos == x.pos, (elem for elem in list(openList.queue))) and (currentNode.g + 1 > child.g)): # correct?
                    continue

            # Update cost values
            child.g = currentNode.g + 1
            child.h = ((child.pos[0] - goalNode.pos[0]) ** 2) + ((child.pos[1] - goalNode.pos[1]) ** 2)
            child.f = child.g + child.h
            child.parent = currentNode

            # Add child to open list as a node.
            openList.put(child)
