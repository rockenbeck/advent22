from advent_2022_inputs import *

import re
from collections import defaultdict

test22="""        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""


def day22(lines):
    maplines, path = lines.split("\n\n")

    map = {}
    path = list(path)

    ymax = len(maplines.split('\n'))
    xmax = len(maplines.split('\n')[0])

    xmins = defaultdict(lambda : 1000000)
    xmaxs = defaultdict(lambda : -1000000)
    ymins = defaultdict(lambda : 1000000)
    ymaxs = defaultdict(lambda : -1000000)

    start = None
    for y,line in enumerate(maplines.split('\n')):
        for x,ch in enumerate(line):
            
            if ch == '.':
                if start == None:
                    start = (x,y)
            if ch != ' ':
                map[(x,y)] = ch

                xmins[y] = min(xmins[y], x)
                xmaxs[y] = max(xmaxs[y], x)
                ymins[x] = min(ymins[x], y)
                ymaxs[x] = max(ymaxs[x], y)
                
    (x,y) = start
    facing = 0 # right

    while len(path) > 0:
        c = path.pop(0)
        if c == 'L':
            facing = (facing - 1) % 4
        elif c == 'R':
            facing = (facing + 1) % 4
        else:
            assert(c.isdigit())
            s = c
            while len(path) > 0 and path[0].isdigit():
                s = s + path.pop(0)
            n = int(s)

            for i in range(0,int(s)):
                if facing == 0:
                    xNext,yNext = x + 1, y
                    if (xNext,yNext) not in map:
                        xNext = xmins[y]
                elif facing == 1:
                    xNext,yNext = x, y + 1
                    if (xNext,yNext) not in map:
                        yNext = ymins[x]
                elif facing == 2:
                    xNext,yNext = x - 1, y
                    if (xNext,yNext) not in map:
                        xNext = xmaxs[y]
                elif facing == 3:
                    xNext,yNext = x, y - 1
                    if (xNext,yNext) not in map:
                        yNext = ymaxs[x]
                else:
                    assert(False)

                if map[xNext,yNext] == '.':
                    x,y = xNext,yNext
                else:
                    assert(map[xNext,yNext] == '#')
                    break
    
    print(f"{(x, y, facing) = }, password = {1000 * (y + 1) + (x + 1) * 4 + facing}")

# day22(test22)
# day22(input22)

# test
#   0
# 123
#   45

# input
#  01
#  2
# 34
# 5

def day22b(lines):
    maplines, path = lines.split("\n\n")

    map = {}
    path = list(path)

    # ymax = len(maplines.split('\n'))
    # xmax = len(maplines.split('\n')[0])

    # xmins = defaultdict(lambda : 1000000)
    # xmaxs = defaultdict(lambda : -1000000)
    # ymins = defaultdict(lambda : 1000000)
    # ymaxs = defaultdict(lambda : -1000000)

    start = None
    for y,line in enumerate(maplines.split('\n')):
        for x,ch in enumerate(line):
            
            if ch == '.':
                if start == None:
                    start = (x,y)
            if ch != ' ':
                map[(x,y)] = ch

                # xmins[y] = min(xmins[y], x)
                # xmaxs[y] = max(xmaxs[y], x)
                # ymins[x] = min(ymins[x], y)
                # ymaxs[x] = max(ymaxs[x], y)
                
    (x,y) = start
    facing = 0 # right

    steps = 0
    while len(path) > 0:
        c = path.pop(0)
        if c == 'L':
            facing = (facing - 1) % 4
        elif c == 'R':
            facing = (facing + 1) % 4
        else:
            assert(c.isdigit())
            s = c
            while len(path) > 0 and path[0].isdigit():
                s = s + path.pop(0)
            n = int(s)
            steps += 1

            # Hard-coded face layout for main puzzle, like so:
            #  01
            #  2
            # 34
            # 5
            # Would be cooler, but considerably more difficult, to make this automatic

            for i in range(0,int(s)):
                if facing == 0:
                    xNext,yNext,facingNext = x + 1, y, facing
                    if (xNext,yNext) not in map:
                        if y < 50:
                            xNext,yNext,facingNext = 99,149-y,2
                        elif y < 100:
                            xNext,yNext,facingNext = 50+y,49,3
                        elif y < 150:
                            xNext,yNext,facingNext = 149,149-y,2
                        else:
                            xNext,yNext,facingNext = y-100,149,3
                elif facing == 1:
                    xNext,yNext,facingNext = x, y + 1, facing
                    if (xNext,yNext) not in map:
                        if x < 50:
                            xNext,yNext = x+100,0
                        elif x < 100:
                            xNext,yNext,facingNext = 49,x+100,2
                        else:
                            xNext,yNext,facingNext = 99,x-50,2
                elif facing == 2:
                    xNext,yNext,facingNext = x - 1, y, facing
                    if (xNext,yNext) not in map:
                        if y < 50:
                            xNext,yNext,facingNext = 0,149-y,0
                        elif y < 100:
                            xNext,yNext,facingNext = y-50,100,1
                        elif y < 150:
                            xNext,yNext,facingNext = 50,49-(y-100),0
                        else:
                            xNext,yNext,facingNext = y-100,0,1
                elif facing == 3:
                    xNext,yNext,facingNext = x, y - 1, facing
                    if (xNext,yNext) not in map:
                        if x < 50:
                            xNext,yNext,facingNext = 50,x+50,0
                        elif x < 100:
                            xNext,yNext,facingNext = 0,100+x,0
                        else:
                            xNext,yNext = x-100,199
                else:
                    assert(False)

                if map[(xNext,yNext)] == '.':
                    x,y,facing = xNext,yNext,facingNext
                else:
                    assert(map[(xNext,yNext)] == '#')
                    break
    
    print(f"{(x, y, facing) = }, password = {1000 * (y + 1) + (x + 1) * 4 + facing}")

# day22(test22)
day22b(input22)
