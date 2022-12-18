from advent_2022_inputs import *


test18 = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""


def day18(lines):
    cubes = set()
    for line in lines.split("\n"):
        x,y,z = map(int, line.split(','))
        cubes.add((x,y,z))

    sides = 0
    for (x,y,z) in cubes:
        sides += 6
        for dx,dy,dz in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
            if (x+dx,y+dy,z+dz) in cubes:
                sides -= 1

    print(f"Part A = {sides}")

    xMin = min(cube[0] for cube in cubes)
    xMax = max(cube[0] for cube in cubes)
    yMin = min(cube[1] for cube in cubes)
    yMax = max(cube[1] for cube in cubes)
    zMin = min(cube[2] for cube in cubes)
    zMax = max(cube[2] for cube in cubes)
    print(f"({xMin},{yMin},{zMin}) - ({xMax},{yMax},{zMax})")

    start = (xMin - 1, yMin - 1, zMin - 1)
    tests = {start}
    ext = {start}

    while len(tests) > 0:
        (x,y,z) = tests.pop()
        for dx,dy,dz in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
            (xT,yT,zT) = (x+dx,y+dy,z+dz)
            if xT < xMin-1 or xT > xMax+1 or yT < yMin-1 or yT > yMax+1 or zT < zMin-1 or zT > zMax+1:
                continue
            if (xT,yT,zT) in cubes:
                continue
            if (xT,yT,zT) in ext:
                continue
            ext.add((xT,yT,zT))
            tests.add((xT,yT,zT))

    # print(ext)

    sidesExt = 0
    for (x,y,z) in cubes:
        for dx,dy,dz in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
            if (x+dx,y+dy,z+dz) in ext:
                sidesExt += 1

    print(f"Part B = {sidesExt}")



# day18(test18)
day18(input18)