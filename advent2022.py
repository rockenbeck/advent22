from advent_2022_inputs import *

import re
from collections import defaultdict
import sys
import random
import math
#from math import *

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
day6b(input6)
