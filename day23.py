from advent_2022_inputs import *

import re
from collections import defaultdict

test23="""....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#.."""

def printMap(i,map):
    xMin = min(elf[0] for elf in map)
    yMin = min(elf[1] for elf in map)
    xMax = max(elf[0] for elf in map)
    yMax = max(elf[1] for elf in map)

    print(f"== End of Round {i}")
    for y in range(yMin,yMax + 1):
        s = ""
        for x in range(xMin,xMax+1):
            s = s + ('#' if (x,y) in map else '.')
        print(s)

def day23(lines):
    map = set()

    for y,line in enumerate(lines.split("\n")):
        for x,ch in enumerate(line):
            if ch == "#":
                map.add((x,y))
    
    # printMap(0,map)

    checks = [[(-1,-1),(0,-1),(1,-1)],
              [(-1,1),(0,1),(1,1)],
              [(-1,-1),(-1,0),(-1,1)],
              [(1,-1),(1,0),(1,1)]]
    # for i in range(0,10): # part A
    
    anyMoved = True
    i = 0
    while anyMoved:
        anyMoved = False
        mapNew = set()
        moves = {}
        dests = defaultdict(lambda : 0)

        for x,y in map:
            cAdj = 0
            for dY in [-1,0,1]:
                for dX in [-1,0,1]:
                    if (x+dX,y+dY) in map:
                        cAdj += 1
            xProp,yProp = x,y
            if cAdj > 1:
                for dir in range(0,4):
                    check = checks[(dir + i) % 4]
                    blocked = False
                    for dx,dy in check:
                        if (x+dx,y+dy) in map:
                            blocked = True
                            break
                    if not blocked:
                        xProp,yProp = x+check[1][0],y+check[1][1]
                        break
            moves[(x,y)] = (xProp,yProp)
            dests[(xProp,yProp)] = dests[(xProp,yProp)] + 1
        
        for (x,y),(xProp,yProp) in moves.items():
            if dests[(xProp,yProp)] == 1:
                mapNew.add((xProp,yProp))
                if xProp != x or yProp != y:
                    anyMoved = True
            else:
                mapNew.add((x,y))
        map = mapNew

        # printMap(i+1,map)
        if not anyMoved:
            break
        i += 1

    xMin = min(elf[0] for elf in map)
    yMin = min(elf[1] for elf in map)
    xMax = max(elf[0] for elf in map)
    yMax = max(elf[1] for elf in map)

    empty = 0
    for y in range(yMin,yMax + 1):
        for x in range(xMin,xMax+1):
            if (x,y) not in map:
                empty += 1

    print(f"Round {i+1} {empty = }")

# day23(test23)
day23(input23)


