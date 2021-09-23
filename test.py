from queue import PriorityQueue
from util import Node

node1 = Node(None, (1,1))
node2 = Node(None, (2,2))
node3 = Node(None, (3,3))

node1.f = 5
node2.f = 10
node3.f = 20



q = PriorityQueue()

q.put((node1))
q.put((node2))
q.put((node3))


print(q.get().f)
print(q.get().f)
print(q.get().f)
