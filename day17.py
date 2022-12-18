from advent_2022_inputs import *

test17 = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""

def collide(map, rock, pos):
    for dpos in rock:
        x,y = pos[0] + dpos[0], pos[1] + dpos[1]
        if (x,y) in map:
            return True
        if x < 0 or x >= 7:
            return True
        if y < 0:
            return True
    return False

def day17(gusts, crock):
    rocks = [[(0,0),(1,0),(2,0),(3,0)],
             [(0,1),(1,0),(1,1),(1,2),(2,1)],
             [(0,0),(1,0),(2,0),(2,1),(2,2)],
             [(0,0),(0,1),(0,2),(0,3)],
             [(0,0),(0,1),(1,0),(1,1)]]

    map = set()

    iRock = 0
    iGust = 0
    yMax = 0

    starts = {}

    for i in range(0,crock):
        # found cycle by examining this output
        # what's an elegant way to automate this?
        # if (iRock, iGust) in starts:
        #     iPrev,yMaxPrev = starts[(iRock, iGust)]
        #     print(f"{i = } previous {i - iPrev} rocks ago, dy = {yMax - yMaxPrev}")
        # starts[(iRock,iGust)] = (i, yMax)

        y = yMax + 3
        x = 2
        rock = rocks[iRock]
        iRock = (iRock + 1) % len(rocks)

        while True:
            xT = x + (1 if gusts[iGust] == '>' else -1)
            iGust = (iGust + 1) % len(gusts)
            x = x if collide(map, rock, (xT, y)) else xT
            if collide(map, rock, (x, y - 1)):
                break
            y -= 1

        for dpos in rock:
            yMax = max(yMax, y + dpos[1] + 1)
            map.add((x + dpos[0], y + dpos[1]))
    
        # yMax = max(map, key=lambda pos: pos[1])[1] + 1
        # for yT in range(yMax - 1, -1, -1):
        #     s = ""
        #     for xT in range(0,7):
        #         s = s + ('#' if (xT,yT) in map else '.')
        #     print(s)

    return yMax

print(f"{day17(test17, 2022) = }") # cycle starts at i = 50, 35 long, dy = 53
print(f"{day17(input17, 2022) = }") # cycle starts at i = 1855, 1725 long, dy = 2659

def day17b(gusts, crock, iCycleStart, cycle, dyPerCycle):
    cCycleSkip = (crock - iCycleStart) // cycle
    dySkip = cCycleSkip * dyPerCycle
    dyLeft = day17(gusts, crock - cCycleSkip * cycle)
    print(f"{dySkip + dyLeft = }")

day17b(test17, 1000000000000, 50, 35, 53)
day17b(input17, 1000000000000, 1855, 1725, 2659)
