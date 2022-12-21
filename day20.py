from advent_2022_inputs import *

import re
from collections import defaultdict


test20 = """1
2
-3
3
-2
0
4"""

class Node:
    def __init__(self, n) -> None:
        self.prev = None
        self.next = None
        self.n = n

    def move(self, d):
        # print(f"move {d}")
        prev = self.prev
        self.next.prev = self.prev
        self.prev.next = self.next
        while d < 0:
            prev = prev.prev
            d += 1
        while d > 0:
            prev = prev.next
            d -= 1
        self.prev = prev
        self.next = prev.next
        prev.next = self
        self.next.prev = self
    
    def advance(self, d):
        node = self
        for i in range(0,d):
            node = node.next
        return node

def day20(lines):
    
    key=811589153
    c=10

    a = list(map(lambda s: int(s) * key, lines.split("\n")))
    nodes = list(map(Node, a))
    
    for i,node in enumerate(nodes):
        node.prev = nodes[(i-1) % len(nodes)]
        node.next = nodes[(i+1) % len(nodes)]
        if node.n == 0:
            node0 = node
        if node.n == 1:
            node1 = node

    # nodes.sort(key = lambda node: node.n)

    for i in range(0,c):
        # nodeT = node0
        # s = ""
        # while True:
        #     s = s + str(nodeT.n) + " "
        #     nodeT = nodeT.next
        #     if nodeT == node0:
        #         break
        # print(s)

        for node in nodes:
            node.move(node.n % (len(nodes) - 1))

    
    node1000 = node0.advance(1000)
    node2000 = node1000.advance(1000)
    node3000 = node2000.advance(1000)

    print(f"{node1000.n + node2000.n + node3000.n = }")

# day20(test20)
day20(input20)