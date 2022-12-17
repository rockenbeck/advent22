from advent_2022_inputs import *

import re
from collections import defaultdict
import sys
import random
import math
#from math import *
import numpy as np

#from intcode import *

def day1a(s):
    elves = [0]
    for line in s.split('\n'):
        if len(line) == 0:
            elves.append(0)
        else:   
            n = int(line)
            elves[-1] += n
    print(elves, max(elves))
    elves.sort()
    print(elves[-5:], sum(elves[-3:]))

test1="""1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

#day1a(input1)
#day1b(input1)



def day2a(s):
    total = 0
    for line in s.split('\n'):
        him = line[0]
        me = line[2]
        if (him=='A' and me=='X') or (him=='B' and me=='Y') or (him=='C' and me=='Z'):
            #draw
            score = 3
        elif (him=='A' and me=='Y') or (him=='B' and me=='Z') or (him=='C' and me=='X'):
            # win
            score = 6
        else:
            score = 0
        #print(score)
        score += ord(me) - ord('X') + 1
        total += score
        #print(score)
    print(total)

def day2a_good(s):
    total = 0
    for line in s.split('\n'):
        him = ord(line[0]) - ord('A')
        me = ord(line[2]) - ord('X')
        total += [0, 6, 3][me - him] + me + 1
    print(total)

def day2b(s):
    total = 0
    for line in s.split('\n'):
        him = line[0]
        me = line[2]
        if me=='Y':
            #draw
            score = 3
            if him=='A':
                score += 1
            elif him=='B':
                score += 2
            else:
                score += 3
        elif me=='Z':
            # win
            score = 6
            if him=='A':
                score += 2
            elif him=='B':
                score += 3
            else:
                score += 1
        else:
            #lose
            score = 0
            if him=='A':
                score += 3
            elif him=='B':
                score += 1
            else:
                score += 2
        #print(score)
        total += score
        #print(score)
    print(total)

def day2b_good(s):
    total = 0
    for line in s.split('\n'):
        him = ord(line[0]) - ord('A')
        me = (him + ord(line[2]) - ord('X') - 1) % 3
        total += [0, 6, 3][me - him] + me + 1
    print(total)


test2="""A Y
B X
C Z"""

# day2b(test2)
# day2b(input2)
# day2a_good(test2)
# day2b_good(input2)



def day3a(s):
    total = 0
    for line in s.split('\n'):
        c = len(line) // 2
        s = set()
        for ch in line[:c]:
            s.add(ch)
        for ch in line[c:]:
            if ch in s:
                break
        #print(ch)
        if ch >= 'a' and ch <= 'z':
            prio = ord(ch) - ord('a') + 1
        else:
            prio = ord(ch) - ord('A') + 27
        total += prio
    print(total)

def day3b(s):
    total = 0
    lines = s.split('\n')

    for i in range(0,len(lines),3):
        s1 = set()
        for ch in lines[i]:
            s1.add(ch)
        s2 = set()
        for ch in lines[i+1]:
            s2.add(ch)
        for ch in lines[i+2]:
            if ch in s1 and ch in s2:
                break
        print(ch)
        if ch >= 'a' and ch <= 'z':
            prio = ord(ch) - ord('a') + 1
        else:
            prio = ord(ch) - ord('A') + 27
        total += prio
    print(total)

test3="""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

#day3b(input3)

def day4a(s):
    tot = 0
    for line in s.split('\n'):
        [a,b] = line.split(',')
        [amin, amax] = map(int, a.split('-'))
        [bmin, bmax] = map(int, b.split('-'))
        #print(amin,amax,bmin,bmax)
        if (amin >= bmin and amax <= bmax) or (amin <= bmin and amax >= bmax):
            #print("in")
            tot += 1
    print(tot)

def day4b(s):
    tot = 0
    for line in s.split('\n'):
        [a,b] = line.split(',')
        [amin, amax] = map(int, a.split('-'))
        [bmin, bmax] = map(int, b.split('-'))
        #print(amin,amax,bmin,bmax)
        if not (amax < bmin or bmax < amin):
            #print("in")
            tot += 1
    print(tot)

test4="""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

#day4a(input4)
# day4b(input4)



def day5(s):
    cpile = 0
    fend = False
    for line in s.split('\n'):
        if not fend:
            if cpile == 0:
                cpile = (len(line) + 1) // 4
                stacks = [""] * cpile
            if line[1] == '1':
                fend = True
                continue
            for i in range(0,cpile):
                c = line[i * 4 + 1]
                if c != ' ':
                    stacks[i] = stacks[i] + c
        else:
            if len(line) == 0:
                continue
            match = re.match(r"""move\s(?P<N>[0-9]+)\sfrom\s(?P<from>[0-9]+)\sto\s(?P<to>[0-9]+)""", line)
            if not match:
                print("can't parse", line)
                return
            gd = match.groupdict()
            n = int(gd["N"])
            f = int(gd["from"]) - 1
            t = int(gd["to"]) - 1
            x = stacks[f][0:n]
            stacks[f] = stacks[f][n:]
            # stacks[t] = x[::-1] + stacks[t] # part A
            stacks[t] = x[::1] + stacks[t] # part B

    print(''.join([sz[0] for sz in stacks]))


test5="""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


# day5(input5)


def day6a(s):
    for i in range(3,len(s)):
        if s[i-3] == s[i-2] or s[i-3] == s[i-1] or s[i-3] == s[i]:
            continue
        if s[i-2] == s[i-1] or s[i-2] == s[i] or s[i-1] == s[i]:
            continue
        break
    print(i + 1)

def day6b(s):
    n = 14
    for i in range(n-1,len(s)):
        c = set()
        for ch in s[i-n+1:i+1]:
            c.add(ch)
        if len(c) == n:
            break
    print(i + 1)

test6="""nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""

# day6b(test6)
# day6b(input6)




test7="""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

class Dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        if parent != None:
            parent.subdirs[name] = self
        self.subdirs = {}
        self.size = 0
        self.total = 0

def PrintDir(dir, indent=0):
    print(' ' * indent + '- ' + dir.name + " total:", dir.total)
    for s in dir.subdirs.values():
        PrintDir(s, indent+1)

def CalcTotals(dir):
    dir.total = dir.size
    for s in dir.subdirs.values():
        dir.total += CalcTotals(s)
    return dir.total

def Sum(dir):
    score = dir.total if dir.total <= 100000 else 0
    for s in dir.subdirs.values():
        score += Sum(s)
    return score
    
def BestDir(dir, needed):
    best = None
    if dir.total >= needed:
        best = dir
    for s in dir.subdirs.values():
        subbest = BestDir(s, needed)
        if subbest != None:
            if best == None:
                best = subbest
            elif subbest.total < best.total:
                best = subbest
    return best
    
def day7a(s):
    inls = False
    root = Dir('/')
    cur = root
    for line in s.split('\n'):
        if line[0] == "$":
            inls = False
            if line[2:] == "ls":
                inls = True
            elif line[2:4] == 'cd':
                name = line[5:]
                if name=='/':
                    cur = root
                elif name=='..':
                    cur = cur.parent
                else:
                    if name in cur.subdirs:
                        cur = cur.subdirs[name]
                    else:
                        cur = Dir(name, cur)
            else:
                assert(False)
        else:
            assert(inls)
            cb,name = line.split(' ')
            if cb=="dir":
                if name not in cur.subdirs:
                    Dir(name, cur)
            else:
                cur.size += int(cb)

    CalcTotals(root)
    # print(Sum(root))
    PrintDir(root)
    needed = root.total - 40000000
    print(f"{needed = }")
    best = BestDir(root, needed)
    print("best to delete =", best.name, best.total)

# day7a(test7)
# day7a(input7)


test8="""30373
25512
65332
33549
35390"""

def day8a(s):
    grid = s.split("\n")
    
    cx = len(grid[0])
    cy = len(grid)

    a = np.zeros((cy,cx),dtype=int)

    for y in range(0,cy):
        for x in range(0,cx):
            a[y,x] = grid[y][x]
    # print(a)

    maxW = np.zeros((cy,cx), int)
    maxE = np.zeros((cy,cx), int)
    for y in range(0,cy):
        n = -1
        for x in range(0,cx):
            maxW[y,x] = n
            n = max(n,a[y,x])
        n = -1
        for x in range(cx-1,-1,-1):
            maxE[y,x] = n
            n = max(n,a[y,x])
    # print(maxW)
    # print(maxE)

    maxN = np.zeros((cy,cx), int)
    maxS = np.zeros((cy,cx), int)
    for x in range(0,cx):
        n = -1
        for y in range(0,cy):
            maxN[y,x] = n
            n = max(n,a[y,x])
        n = -1
        for y in range(cy-1,-1,-1):
            maxS[y,x] = n
            n = max(n,a[y,x])
    # print(maxN)
    # print(maxS)

    total = 0

    # vis = np.zeros((cy,cx), int)
    for x in range(0,cx):
        for y in range(0,cy):
            if a[y,x] > maxN[y,x] or a[y,x] > maxS[y,x] or a[y,x] > maxE[y,x] or a[y,x] > maxW[y,x]:
                total += 1
                # vis[y,x]=1

    # print(vis)
    print(total)

def day8b(s):
    grid = s.split("\n")
    cx = len(grid[0])
    cy = len(grid)

    a = np.zeros((cy,cx),int)

    for y in range(0,cy):
        for x in range(0,cx):
            a[y,x] = grid[y][x]
    # print(a)

    scores = np.zeros((cy,cx),int)

    best = 0
    for y in range(0,cy):
        for x in range(0,cx):
            dW = 0
            for xT in range(x-1,-1,-1):
                dW += 1
                if a[y,xT] >= a[y,x]:
                    break

            dE = 0
            for xT in range(x + 1,cx):
                dE += 1
                if a[y,xT] >= a[y,x]:
                    break

            dN = 0
            for yT in range(y-1,-1,-1):
                dN += 1
                if a[yT,x] >= a[y,x]:
                    break

            dS = 0
            for yT in range(y + 1,cy):
                dS += 1
                if a[yT,x] >= a[y,x]:
                    break
            score = dN * dS * dE * dW
            # print(dN, dS, dE, dW, score)
            scores[y,x] = score
            best = max(best, score)

    # print(scores)
    print(best)
            
def day8b_better(s):
    grid = s.split("\n")
    cx = len(grid[0])
    cy = len(grid)

    a = np.zeros((cy,cx),int)

    for y in range(0,cy):
        for x in range(0,cx):
            a[y,x] = grid[y][x]
    # print(a)

    # scores = np.zeros((cy,cx),int)

    best = 0
    for y in range(0,cy):
        for x in range(0,cx):
            # not sure this is actually better
            # make xT,yT a numpy vector?

            dists = []
            for (dy,dx) in [(-1,0),(1,0),(0,1),(0,-1)]:
                xT,yT = x+dx, y+dy
                dist = 0
                while xT >= 0 and xT < cx and yT >= 0 and yT < cy:
                    dist += 1
                    if a[yT,xT] >= a[y,x]:
                        break
                    xT += dx
                    yT += dy
                dists.append(dist)
            score = math.prod(dists)
            # print(dists, score)
            # scores[y,x] = score
            best = max(best, score)

    # print(scores)
    print(best)
            
# day8b(test8)
# day8b(input8)
# day8b_better(input8)

test9="""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

def sign(n):
    if n == 0:
        return 0
    return 1 if n > 0 else -1

def follow(h, t):
    if abs(h[0] - t[0]) > 1 or abs(h[1] - t[1]) > 1:
        t = (t[0] + sign(h[0] - t[0]), t[1] + sign(h[1] - t[1]))
    return t

def day9a(s,l):
    h = (0,0)
    ts = [(0,0)] * l

    dirs = {'U': (0,1), 'D': (0,-1), 'L': (-1,0), 'R': (1,0)}

    visits = set()
    visits.add(ts[-1])

    for line in s.split("\n"):
        dir,n = line.split(" ")
        dxy = dirs[dir]
        for i in range(0,int(n)):
            h = (h[0] + dxy[0], h[1] + dxy[1])
            p = h
            tsNew = []
            for t in ts:
                tsNew.append(p := follow(p,t))
            ts = tsNew
            print(f"{ts=}")
            visits.add(ts[-1])

    print(len(visits))

# day9a(input9,9)

test10="""noop
addx 3
addx -5"""

def day10(s):
    cycle = 1
    ip = 0
    lines = s.split("\n")
    inAdd = False
    x = 1
    dx = 0
    xs = []

    cycle = 0
    output = []

    while cycle < 240:
        if inAdd:
            dx = n
            inAdd = False
        else:
            line = lines[ip].split(" ")
            op = line[0]
            if (op == "noop"):
                pass
            elif (op == "addx"):
                n = int(line[1])
                inAdd = True
            else:
                assert(False)
            ip += 1

        xs.append(x)

        output.append("#" if abs(x - (cycle % 40)) < 2 else ".")

        cycle += 1
        if cycle % 40 == 0:
            output.append("\n")

        x += dx
        dx = 0

    strengths = list(map(lambda i: xs[i - 1] * i, [20, 60, 100, 140, 180, 220]))
    # print(f"{strengths=}")
    # print(sum(strengths))
    print("".join(output))
    
# day10(test10b)
# day10(input10)



test11="""Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

monkeys = []
monkeymod = 0

class Monkey:
    def __init__(self, s):
        lines = s.split("\n")

        gd = re.match(r"""\s*Starting items: (?P<items>[0-9, ]+)""", lines[1]).groupdict()
        # gd = re.match(r"""\s*Starting items: (?P<items>.+)""", lines[1]).groupdict()
        self.items = list(map(int, gd["items"].split(", ")))

        gd = re.match(r"""\s*Operation: new = old (?P<op>[\+\*]) (?P<arg>.+)""", lines[2]).groupdict()
        self.op = gd["op"]
        self.arg = gd["arg"]

        gd = re.match(r"""\s*Test: divisible by (?P<divby>[0-9]+)""", lines[3]).groupdict()
        self.divby = int(gd["divby"])

        gd = re.match(r"""\s*If true: throw to monkey (?P<to>[0-9]+)""", lines[4]).groupdict()
        self.iftrue = int(gd["to"])
        
        gd = re.match(r"""\s*If false: throw to monkey (?P<to>[0-9]+)""", lines[5]).groupdict()
        self.iffalse = int(gd["to"])

        self.inspect = 0
        
    def __repr__(self):
        return f"[{self.items=} {self.op=} {self.arg=} {self.divby=} {self.iftrue=} {self.iffalse=} {self.inspect=}]"

    def exec(self):
        global monkeys
        global monkeymod

        while len(self.items) > 0:
            item =self.items.pop(0)

            self.inspect += 1

            if self.arg == "old":
                n = item
            else:
                n = int(self.arg)

            if self.op == "+":
                item = (item + n) % monkeymod
            elif self.op == "*":
                # (A * B) mod C = (A mod C * B mod C) mod C
                # but this is wrong, because we're tossing items between monekys with different Cs:
                # item = ((item % self.divby) * (n % self.divby)) % self.divby
                # so we need to use the product of all the monkeys in the list
                item = ((item % monkeymod) * (n % monkeymod)) % monkeymod
            else:
                assert(False)
            
            # item //= 3 part A

            throwto = self.iftrue if item % self.divby == 0 else self.iffalse
            monkeys[throwto].items.append(item)

def day11(s):
    global monkeys
    global monkeymod
    
    for m in s.split("\n\n"):
        monkeys.append(Monkey(m))

    # print(monkeys)

    monkeymod = math.prod([monkey.divby for monkey in monkeys])
    print(f"{monkeymod=}")

    # for round in range(0,1):
    for round in range(0,10000):
        for monkey in monkeys:
            monkey.exec()

        # for i,monkey in enumerate(monkeys):
        #     print(f"Monkey {i}:", monkey.items)

    print(f"After {round+1} rounds")
    for i,monkey in enumerate(monkeys):
        print(f"Monkey {i}:", monkey.inspect)

    sm = sorted(monkeys, key = lambda monkey: monkey.inspect, reverse=True)
    # print(sm)

    print(sm[0].inspect * sm[1].inspect)

# day11(test11)
# day11(input11)



test12="""Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


def day12a(s):
    map = {}
    for y,line in enumerate(s.split("\n")):
        for x,ch in enumerate(line):
            if ch == 'S':
                start = (x,y)
                ch = 'a'
            elif ch == 'E':
                end = (x,y)
                ch = 'z'
            map[(x,y)] = ord(ch) - ord('a')

    front = {start}
    bestdist = {start: 0}

    while len(front):
        (x,y) = front.pop()
        h = map[(x,y)]
        dist = bestdist[(x,y)]
        for (dx,dy) in [(-1,0),(1,0),(0,-1),(0,1)]:
            new = (x+dx,y+dy)
            if new not in map:
                continue # off edge
            if map[new] > h + 1:
                continue # too tall
            if new not in bestdist or dist + 1 < bestdist[new]:
                bestdist[new] = dist + 1
                front.add(new)
    
    print(bestdist[end])

# day12a(input12)


def day12b(s):
    map = {}
    for y,line in enumerate(s.split("\n")):
        for x,ch in enumerate(line):
            if ch == 'S':
                start = (x,y)
                ch = 'a'
            elif ch == 'E':
                end = (x,y)
                ch = 'z'
            map[(x,y)] = ord(ch) - ord('a')

    front = {end}
    bestdist = {end: 0}

    while len(front):
        (x,y) = front.pop()
        h = map[(x,y)]
        dist = bestdist[(x,y)]
        for (dx,dy) in [(-1,0),(1,0),(0,-1),(0,1)]:
            new = (x+dx,y+dy)
            if new not in map:
                continue # off edge
            if h > map[new] + 1:
                continue # too tall
            if new not in bestdist or dist + 1 < bestdist[new]:
                bestdist[new] = dist + 1
                front.add(new)
    
    starts = []
    for (x,y),h in map.items():
        if h == 0 and (x,y) in bestdist:
            starts.append(bestdist[(x,y)])
    print(min(starts))

# day12b(input12)



test13="""[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

def compareLists(left, right):
    isLeftInt = isinstance(left, int)
    isRightInt = isinstance(right, int)

    if isLeftInt and isRightInt:
        return right - left
    
    if isLeftInt:
        left = [left]
    if isRightInt:
        right = [right]
    
    while len(left) > 0 and len(right) > 0:
        # d = compareLists(left.pop(0), right.pop(0)) modifies inputs, doesn't work for part B
        d = compareLists(left[0], right[0])
        left = left[1:]
        right = right[1:]
        if d != 0:
            return d

    return len(right) - len(left)
    


def day13a(s):
    sum = 0
    for i,pair in enumerate(s.split("\n\n")):
        left = eval(pair.split("\n")[0])
        right = eval(pair.split("\n")[1])
        if compareLists(left, right) > 0:
            sum += i + 1

    print(f"{sum = }")

# day13a(test13)
# day13a(input13)

from functools import cmp_to_key

def day13b(s):
    d2 = [[2]]
    d6 = [[6]]
    lists = [d2,d6]
    for line in s.split("\n"):
        if len(line) > 0:
            lists.append(eval(line))
    
    # lists.sort(cmp = compareLists) #deprecated in Python3 :-(
    lists.sort(key = cmp_to_key(compareLists), reverse=True)
    
    for i,l in enumerate(lists):
        if l == d2:
            i2 = i + 1
        elif l == d6:
            i6 = i + 1

    print(i2 * i6)

# day13b(test13)
# day13b(input13)



test14="""498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

def parseXY(s):
    return tuple(map(int, s.split(",")))

def day14(lines):
    map = {}
    ymax = 0
    for line in lines.split("\n"):
        l = line.split(" -> ")
        s = parseXY(l[0])
        for se in l[1:]:
            e = parseXY(se)

            dx,dy = sign(e[0]-s[0]), sign(e[1]-s[1])
            # print(dx,dy)
            while s != e:
                map[s] = '#'
                s = (s[0]+dx,s[1]+dy)
                ymax = max(ymax, s[1])
            map[e] = '#'

    # print(map)
    # return

    total = 0

    s = (500,0)
    while s not in map:
        (x,y) = s
        while y <= ymax + 2:
            # print(f"{(x,y)}")
            if y == ymax + 1: # part B
                map[(x,y)] = 'o'
                total += 1
                break
            if (x,y+1) in map:
                if (x-1,y+1) in map:
                    if (x+1,y+1) in map:
                        map[(x,y)] = 'o'
                        total += 1
                        break
                    else:
                        (x,y) = (x+1, y+1)
                else:
                    (x,y) = (x-1,y+1)
            else:
                (x,y) = (x,y+1)

        if y > ymax + 2:
            break

    print(total)

# day14(test14)
# day14(input14)


test15="""Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

def addrange(ranges, new):
    i = 0
    while i < len(ranges) and new[0] >= ranges[i][0]:
        i += 1
    ranges.insert(i, new)

    if i > 0:
        i -= 1

    while i + 1 < len(ranges):
        if ranges[i][1] + 1 >= ranges[i+1][0]:
            ranges[i] = (ranges[i][0], max(ranges[i][1], ranges[i+1][1]))
            ranges.pop(i+1)
        else:
            i += 1
    
    # print(ranges)

def intersectrange(ranges, range):
    while len(ranges) > 0 and ranges[0][1] <= range[0]:
        ranges.pop(0)
    while len(ranges) > 0 and ranges[-1][0] >= range[1]:
        ranges.pop(-1)
    if len(ranges) > 0:
        ranges[0] = (max(ranges[0][0], range[0]), ranges[0][1])
        ranges[-1] = (ranges[-1][0], min(ranges[-1][1], range[1]))
    # print(ranges)


# ranges=[]
# addrange(ranges, (1,5))
# addrange(ranges, (6,7))
# addrange(ranges, (10,15))
# addrange(ranges, (5,6))
# # addrange(ranges, (3,12))
# intersectrange(ranges, (3,12))

def day15a(lines, ytest):
    ranges = []
    excludes=set()
    for line in lines.split("\n"):
        match = re.match(r"""Sensor at x=(?P<sx>\-*[0-9]+), y=(?P<sy>\-*[0-9]+): closest beacon is at x=(?P<cx>\-*[0-9]+), y=(?P<cy>\-*[0-9]+)""", line)
        gd = match.groupdict()

        sx,sy = int(gd["sx"]),int(gd["sy"])
        if sy == ytest:
            excludes.add(sx)

        cx,cy = int(gd["cx"]),int(gd["cy"])
        if cy == ytest:
            excludes.add(cx)

        d = abs(cx-sx) + abs(cy-sy)
        dtest = d - abs(sy-ytest)
        if dtest >= 0:
            addrange(ranges, (sx - dtest, sx + dtest))
    
    print(ranges, excludes, sum(map(lambda range: range[1] - range[0] + 1, ranges)) - len(excludes))


# day15(test15, 10)
# day15(input15, 2000000)

def line15b(lines, ytest, limit):
    ranges = []
    for line in lines.split("\n"):
        match = re.match(r"""Sensor at x=(?P<sx>\-*[0-9]+), y=(?P<sy>\-*[0-9]+): closest beacon is at x=(?P<cx>\-*[0-9]+), y=(?P<cy>\-*[0-9]+)""", line)
        gd = match.groupdict()

        sx,sy = int(gd["sx"]),int(gd["sy"])
        cx,cy = int(gd["cx"]),int(gd["cy"])
        d = abs(cx-sx) + abs(cy-sy)
        dtest = d - abs(sy-ytest)
        if dtest >= 0:
            addrange(ranges, (sx - dtest, sx + dtest))
    
    intersectrange(ranges, limit)
    if len(ranges) > 1:
        print(ytest, ranges, sum(map(lambda range: range[1] - range[0] + 1, ranges)))

def day15b(lines, limit):
    for ytest in range(0, limit + 1): # assume x, y same limits
        line15b(lines, ytest, (0, limit))

    # the above code runs pretty slowly

def day15b_better(lines, limit):
    # parse text first into array of sensors
    sensors = []
    for line in lines.split("\n"):
        match = re.match(r"""Sensor at x=(?P<sx>\-*[0-9]+), y=(?P<sy>\-*[0-9]+): closest beacon is at x=(?P<cx>\-*[0-9]+), y=(?P<cy>\-*[0-9]+)""", line)
        gd = match.groupdict()

        sx,sy = int(gd["sx"]),int(gd["sy"])
        cx,cy = int(gd["cx"]),int(gd["cy"])
        d = abs(cx-sx) + abs(cy-sy)

        sensors.append((sx,sy,d))

    # check all lines against sensor array
    # still slow
    # sort sensors by ymin, add as they come in, pop as they go out? would it really help much?
    # use fact that some adjacent or overlapping "diamonds" maintain same relative
    #  spacing from line to line
    for y in range(0, limit + 1): # assume x, y same limits
        ranges = []
        for sx,sy,d in sensors:
            dtest = d - abs(sy-y)
            if dtest >= 0:
                addrange(ranges, (sx - dtest, sx + dtest))
        
        intersectrange(ranges, (0, limit))

        if len(ranges) > 1:
            print(ytest, ranges, sum(map(lambda range: range[1] - range[0] + 1, ranges)))
            assert(len(ranges) == 2)
            assert(ranges[0][1] == ranges[1][0] - 2)
            x = ranges[0][1] + 1
            print(x,y,x * 4000000 + y)

# day15b(test15, 20)
# day15b(input15, 4000000)
# day15b_better(input15, 4000000)
# output was 3249288 [(0, 2978644), (2978646, 4000000)] 4000000
# print(f"{2978645 * 4000000 + 3249288 = }")


test16="""Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

class Valve:
    def __init__(self, line) -> None:
        gd = re.match(r"""Valve (?P<valve>[A-Z]+) has flow rate=(?P<rate>[0-9]+); tunnels? leads? to valves? (?P<to>[A-Z, ]+)""", line).groupdict()
        # gd = re.match(r"""\s*Starting items: (?P<items>.+)""", lines[1]).groupdict()
        self.name = gd["valve"]
        self.rate = int(gd["rate"])
        self.namesTo = gd["to"].split(", ")

    def __repr__(self) -> str:
        return f"{self.name=}, {self.rate=}, {self.namesTo=}"

def day16a(lines):
    valves = {}
    for line in lines.split("\n"):
        valve = Valve(line)
        valves[valve.name] = valve
    
    minutes = [{("AA", ()): 0}]    # (location, opened valve names) => score

    for minute in range(1,31):
        newstates = defaultdict(lambda : 0)
        minutes.append(newstates)
        for (name, opened),score in minutes[minute-1].items():
            newstates[(name, opened)] = score # do nothing
            if name not in opened:
                # open valve
                if valves[name].rate > 0:
                    openedNew = tuple(sorted(opened + (name,)))
                    scoreNew = score + valves[name].rate * (30 - minute)
                    prev = newstates[(name, openedNew)]
                    newstates[(name, openedNew)] = max(prev, scoreNew)
            for nameto in valves[name].namesTo:
                # move to nameto
                newstates[(nameto, opened)] = max(newstates[(nameto, opened)], score)

        print(f"{minute = } len = {len(newstates)} max = {max(newstates.values())}")

    # print(valves)

# day16a(test16)
# day16a(input16)

def day16b(lines):
    valves = {}
    for line in lines.split("\n"):
        valve = Valve(line)
        valves[valve.name] = valve
    
    allclosed = tuple(sorted([valve.name for valve in valves.values() if valve.rate > 0]))
    minutes = [{("AA", "AA", allclosed): 0}]    # (me, elephant, closed valves) => score
    scoreMax = 0

    # this is still pretty slow and is considering >6 million states at min 16
    # speed up by ~2x since elephant and I are interchangeable
    # more accurate scorePoss (take movement, opening times into account)

    for minute in range(1,27):
        newstates = defaultdict(lambda : 0)
        minutes.append(newstates)
        for (me, elephant, closed),score in minutes[minute-1].items():
            # max possible score if we were to open all remaining valves now
            scorePoss = score + sum(map(lambda name: valves[name].rate * (26 - minute), closed))
            if scorePoss <= scoreMax:
                continue # why bother

            mes = [(me, closed, score)] # I do nothing
            if me in closed:
                # I open valve
                assert(valves[me].rate > 0)
                closedNew = tuple(name for name in closed if name != me)
                scoreNew = score + valves[me].rate * (26 - minute)
                scoreMax = max(scoreMax, scoreNew)
                mes.append((me, closedNew, scoreNew))
            for nameto in valves[me].namesTo:
                # I move to nameto
                mes.append((nameto, closed, score))

            for (meT, closedT, scoreT) in mes:
                newstates[(meT, elephant, closedT)] = max(newstates[(meT, elephant, closedT)], scoreT) # do nothing
                if elephant in closedT:
                    # elephant opens valve
                    assert(valves[elephant].rate > 0)
                    closedNew = tuple(name for name in closedT if name != elephant)
                    scoreNew = scoreT + valves[elephant].rate * (26 - minute)
                    scoreMax = max(scoreMax, scoreNew)
                    newstates[(meT, elephant, closedNew)] = max(newstates[(meT, elephant, closedNew)], scoreNew)
                for nameto in valves[elephant].namesTo:
                    # elephant moves to nameto
                    newstates[(meT, nameto, closedT)] = max(newstates[(meT, nameto, closedT)], scoreT)


        print(f"{minute = } len = {len(newstates)} {scoreMax = }")

# day16b(test16)
day16b(input16)

