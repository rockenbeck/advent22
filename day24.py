from advent_2022_inputs import *

import re
from collections import defaultdict
import bisect 

test24 = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""

def day24(lines):
    blizzards = []

    for y,line in enumerate(lines.split('\n')[1:-1]):
        cx = len(line) - 2
        for x,ch in enumerate(line[1:-1]):
            if ch == '^':
                blizzards.append(((x,y),(0,-1)))
            elif ch == 'v':
                blizzards.append(((x,y),(0,1)))
            elif ch == '<':
                blizzards.append(((x,y),(-1,0)))
            elif ch == '>':
                blizzards.append(((x,y),(1,0)))
            else:
                assert(ch=='.')
    cy = y + 1

    # print(cx,cy,blizzards)

    states = [((0,-1),0,0,3*(cx-1 + cy+1))] # (x,y),leg,t,est

    expanded = set()

    blocks = defaultdict(lambda : 0) # x,y,t => count of blizzards
    tMax = 0

    closest = 100000000
    tBest = None
    while tBest == None:
        (x,y),leg,t,est = states.pop(-1)
        if ((x,y),leg,t) in expanded:
            continue

        if est < closest:
            closest = est
            print(f"{closest = }, states = {len(states)}, expanded = {len(expanded)}")

        expanded.add(((x,y),leg,t))

        tT = t+1
        if tT > tMax:
            for (xBliz,yBliz),(dxBliz,dyBliz) in blizzards:
                xT = (xBliz + dxBliz * tT) % cx
                yT = (yBliz + dyBliz * tT) % cy
                blocks[(xT,yT,tT)] = blocks[xT,yT,tT] + 1
            tMax = tT

        for dx,dy in [(0,0),(0,-1),(0,1),(-1,0),(1,0)]:
            xT,yT = x+dx, y+dy
            legT = leg

            if xT == cx - 1 and yT == cy:
                if leg == 2:
                    tBest = t + 1
                    break
                elif leg == 0:
                    legT = leg + 1 # reverse
                    # states = [] # none can catch up # why doesn't this work?

            elif xT == 0 and yT == -1:
                if leg == 1:
                    legT = leg + 1
                    # states = [] # none can catch up # why doesn't this work?

            elif xT < 0 or xT >= cx or yT < 0 or yT >= cy:
                assert(len(states) > 0)
                continue # wall
            
            if ((xT,yT),legT,tT) in expanded:
                assert(len(states) > 0)
                continue

            if blocks[(xT,yT,tT)] == 0:

                # estimate remaining distance
                if legT == 0:
                    estT = 2 * (cx-1 + cy+1) + cx-1-xT + cy-yT
                elif legT == 1:
                    estT = (cx-1 + cy+1) + xT + yT+1
                else:
                    assert(legT == 2)
                    estT = cx-1-xT + cy-yT

                stateT = ((xT,yT),legT,tT,estT)
                #bisect.insort(states, stateT, key=lambda s: s[2] + s[3], reverse=True)
                for i in range(len(states),-1,-1):
                    if i == 0:
                        break
                    if states[i-1][2] + states[i-1][3] >= stateT[2] + stateT[3]:
                        break
                states.insert(i,stateT)
            else:
                assert(len(states) > 0)


    print(f"{tBest = }")

# day24(test24)
day24(input24)