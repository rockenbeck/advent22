from advent_2022_inputs import *

import re
from collections import defaultdict



test19="""Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""

class Blueprint:
    def __init__(self, line) -> None:
        gd = re.match(r"""Blueprint [0-9]+: Each ore robot costs (?P<oreore>[0-9]+) ore\. """
                        r"""Each clay robot costs (?P<clayore>[0-9]+) ore\. """
                        r"""Each obsidian robot costs (?P<obsore>[0-9]+) ore and (?P<obsclay>[0-9]+) clay\. """
                        r"""Each geode robot costs (?P<gore>[0-9]+) ore and (?P<gobs>[0-9]+) obsidian\.""", 
                        line).groupdict()

        self.oreore = int(gd["oreore"])
        self.clayore = int(gd["clayore"])
        self.obsore = int(gd["obsore"])
        self.obsclay = int(gd["obsclay"])
        self.gore = int(gd["gore"])
        self.gobs = int(gd["gobs"])

# def day19_too_slow(lines):
#     bps = []
#     for line in lines.split("\n"):
#         bps.append(Blueprint(line))

#     for bp in bps:
#         statesPrev = {(1,0,0,0,0,0,0,0)} # robots + resources
#         # for minute in range(0,24):
#         for minute in range(0,6):
#             states = set()

#             for state in statesPrev:
#                 # produce
#                 stateP = (state[0:4] + (state[4] + state[0], state[5] + state[1], state[6] + state[2], + state[7] + state[3]))

#                 states.add(stateP)
#                 if state[4] >= bp.oreore:
#                     states.add((stateP[0] + 1,) + stateP[1:4] + (stateP[4] - bp.oreore,) + stateP[5:8])
#                 if state[4] >= bp.clayore:
#                     states.add((stateP[0],) + (stateP[1] + 1,) + stateP[2:4] + (stateP[4] - bp.clayore,) + stateP[5:8])
#                 if state[4] >= bp.obsore and state[5] >= bp.obsclay:
#                     states.add((stateP[0:2]) + (stateP[2] + 1,) + stateP[3:4] + (stateP[4] - bp.obsore, stateP[5] - bp.obsclay) + stateP[6:8])
#                 if state[4] >= bp.gore and state[6] >= bp.gobs:
#                     states.add((stateP[0:3]) + (stateP[3] + 1,) + (stateP[4] - bp.gore,) + (stateP[5],) + (stateP[6] - bp.gobs,) + stateP[7:8])

#             statesPrev = states

#             print(f"Minute {minute+1}: {states}")
#             print(f"{len(states) = } ")

c = 0
best = 0
bests = None

import time
class Timer():
    def __init__(self) -> None:
        self.start()

    def start(self):
        self.tickStart = time.perf_counter()

    def __repr__(self) -> str:
        # BB these are highly variable, not accurate?
        tickNow = time.perf_counter()
        return f"{tickNow - self.tickStart:0.3f}s"

timer = Timer()

def day19_recurse(bp, state, tMax, trace):
    global timer
    global best

    robots = state[0]
    res = state[1]
    t = state[2]

    if trace != None:
        print(timer, trace)
    
    # start with score if we just stop making robots
    score = res[3] + (tMax - t) * robots[3]

    # super-conservative max possible score, if we build a geode robot every minute
    # this could be WAAAY better by taking into account construction costs
    # (but it was enough for me to finally get it to run in several minutes)
    scorePoss = score + (tMax - t) * (tMax - t - 1)
    if scorePoss < best:
        return 0

    assert(t <= tMax)

    if t < tMax:
        if t < tMax - 10: # else so close might as well skip this expensive check
            # hard to tune this parameter
            global bests
            if t == 0:
                bests = defaultdict(lambda : []) # initialize list of states indexed by robots
            
            b = bests[robots]
            for stateT in b:
                if res[0] <= stateT[1][0] and \
                    res[1] <= stateT[1][1] and \
                    res[2] <= stateT[1][2] and \
                    res[3] <= stateT[1][3] and \
                    t >= stateT[2]:
                    return 0 # not as good as some other version, so stop recursion

            ib = 0
            while ib < len(b):
                stateT = b[ib]
                if res[0] >= stateT[1][0] and \
                    res[1] >= stateT[1][1] and \
                    res[2] >= stateT[1][2] and \
                    res[3] >= stateT[1][3] and \
                    t <= stateT[2]:
                    b.pop(ib)
                else:
                    ib += 1

            b.append(state)

        states = []

        # build geode robot at first possible time
        if res[2] > 0:
            dT = 1 + max(0, max((bp.gore - res[0] + robots[0] - 1) // robots[0], (bp.gobs - res[2] + robots[2] - 1) // robots[2]))
            if t + dT <= tMax:
                states.append(((robots[0], robots[1], robots[2], robots[3] + 1), 
                            (res[0] - bp.gore + robots[0] * dT, 
                            res[1] + robots[1] * dT, 
                            res[2] - bp.gobs + robots[2] * dT, 
                            res[3] + robots[3] * dT), t + dT))

        # build obsidian robot at first possible time
        if res[1] > 0:
            dT = 1 + max(0, max((bp.obsore - res[0] + robots[0] - 1) // robots[0], (bp.obsclay - res[1] + robots[1] - 1) // robots[1]))
            if t + dT <= tMax:
                states.append(((robots[0], robots[1], robots[2] + 1, robots[3]), 
                            (res[0] - bp.obsore + robots[0] * dT, 
                            res[1] - bp.obsclay + robots[1] * dT, 
                            res[2] + robots[2] * dT, 
                            res[3] + robots[3] * dT), t + dT))

        # build clay robot at first possible time
        dT = 1 + max(0, (bp.clayore - res[0] + robots[0] - 1) // robots[0])
        if t + dT <= tMax:
            states.append(((robots[0], robots[1] + 1, robots[2], robots[3]), 
                        (res[0] - bp.clayore + robots[0] * dT, 
                        res[1] + robots[1] * dT, 
                        res[2] + robots[2] * dT, 
                        res[3] + robots[3] * dT), t + dT))

        # build ore robot at first possible time
        dT = 1 + max(0, (bp.oreore - res[0] + robots[0] - 1) // robots[0])
        if t + dT <= tMax:
            states.append(((robots[0] + 1, robots[1], robots[2], robots[3]), 
                        (res[0] - bp.oreore + robots[0] * dT, 
                        res[1] + robots[1] * dT, 
                        res[2] + robots[2] * dT, 
                        res[3] + robots[3] * dT), t + dT))

        for stateT in states:
            # indent = (" "*tMax)[0:state[2]]
            # print(f"{indent}{stateT}")
            score = max(score, day19_recurse(bp, stateT, tMax, (trace + [stateT]) if trace != None and len(trace) < 3 else None))

    if score > best:
        best = score
        print(timer, f"{best = }")

    return score
    
def day19(lines):
    global timer
    global best

    bps = []
    for line in lines.split("\n"):
        bps.append(Blueprint(line))

    stateStart = ((1,0,0,0),(0,0,0,0),0) # robots, resources, t

    partA = False
    if partA:
        total = 0

        for i,bp in enumerate(bps):
            global timer
            timer.start()
            geodes = day19_recurse(bp, stateStart, 24, [])
            score = geodes * (i + 1)
            total += score
            print(f"Blueprint {i + 1} {geodes = } {score = } {total = }")
    else:
        total = 1
        for i in range(0,3):
            if i == 0:
                geodes = 25
            elif i == 1:
                geodes = 19
            else:
                best = 30 # hack, 'cause I found 31 in a previous run
                bp = bps[i]
                timer.start()
                geodes = day19_recurse(bp, stateStart, 32, [])
            total *= geodes
            print(f"Blueprint {i + 1} {geodes = } {total = }")

# day19(test19)
day19(input19)

# Blueprint 1 geodes = 25 total = 25
# Blueprint 2 geodes = 19 total = 475
# Blueprint 3 geodes = 31 total = 14725

# (1,1,0,0,2,1,0,0) is always better than (1,1,0,0,2,0,0,0) => delete 2nd
# delete ones which won't be able to buy something different by waiting
# will some greedy algorithm get right answer? (super-greedy -> no)
# A*, but how to over-estimate max possible score?
# state can be just order of building robots

# simple to calcuate score from list of moves
# know every winning set of moves must include build clay, build obs, build geode
# could reduce search tree by not stepping by single minutes, but calculating
#  at what minute each type of robot could be built, then stepping forward exactly that much
#  maybe tree isn't all that big? (only millions in this case, but they're expensive to check)