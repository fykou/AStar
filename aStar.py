from queue import PriorityQueue


def aStar(task):
    class Node:
        def __init__(self, pos, parent=None, cost=0):
            self.pos = pos  # task.get_cell_value([x, y])
            self.parent = parent
            self.h = 0  # heuristic cost to goal
            self.g = cost  # cost to node
            self.f = self.h + self.g  # h + g

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
                
            newNode = Node(newPos, currentNode, task.get_cell_value(newPos)) # Create new node on that position and add parent
            children.append(newNode) # Add position to children

        for child in children:

            # Check if current child is in the closed list.
            if (child.pos in closedList):
                    continue

            # Update cost values
            child.g = currentNode.g + child.g
            # child.h = ((goalNode.pos[0] - child.pos[0]) ** 2 + (goalNode.pos[1] - child.pos[1] ) ** 2)**0.5 # Eucledian
            child.h = abs(goalNode.pos[0] - child.pos[0]) + abs(goalNode.pos[1] - child.pos[1]) # Manhattan
            child.f = child.g + child.h
            child.parent = currentNode

            # Check if current child is in the open lists and if the g value is lower than the current node's g value
            if True in map(lambda openNode: child.pos == openNode.pos and child.g > openNode.g, (elem for elem in list(openList.queue))):
                continue

            # Add child to open list as a node.
            openList.put(child)
    
    print("no path found")
    return None
