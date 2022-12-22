from advent_2022_inputs import *

import re
from collections import defaultdict

test21="""root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""

class Monkey:
    def __init__(self, line) -> None:
        self.name,args = line.split(": ")

        if self.name == "humn":
            self.n = "unk"
            return

        if args.isdigit():
            self.op = None
            self.n = int(args)
        else:
            self.argA, self.op, self.argB = args.split(" ")
            if self.op == "/":
                self.op = "//"

            self.n = None
        
        if self.name == "root": # not necessary
            self.op = "="

    def eval(self, monkeys):
        if self.n == None:
            a = monkeys[self.argA].eval(monkeys)
            b = monkeys[self.argB].eval(monkeys)

            if a == "unk" or b == "unk":
                self.n = "unk"
            else:
                self.n = eval(f"{a} {self.op} {b}")
        return self.n

    def force(self, n, monkeys):
        # Force monkey to have value n, by pushing forced values down in tree
        # Might be more elegant to reorder root "=" node of tree to isolate HUMN on one side,
        #  like one would do for regular algebra

        if self.n != "unk":
            return

        if self.name == "humn":
            self.n = n
            return

        assert(self.op != None)

        monkeyA = monkeys[self.argA]
        monkeyB = monkeys[self.argB]
        a = monkeyA.eval(monkeys)
        b = monkeyB.eval(monkeys)

        if self.op == "*":
            if a == "unk":
                monkeyA.force(n // b, monkeys)
            else:
                monkeyB.force(n // a, monkeys)
        elif self.op == "//":
            if a == "unk":
                monkeyA.force(n * b, monkeys)
            else:
                monkeyB.force(a // n, monkeys)
        elif self.op == "+":
            if a == "unk":
                monkeyA.force(n - b, monkeys)
            else:
                monkeyB.force(n - a, monkeys)
        elif self.op == "-":
            if a == "unk":
                monkeyA.force(n + b, monkeys)
            else:
                monkeyB.force(a - n, monkeys)
        else:
            assert(False)

def day21b(lines):
    monkeys = {}
    for line in lines.split("\n"):
        monkey = Monkey(line)
        monkeys[monkey.name] = monkey

    root = monkeys["root"]
    monkeyA = monkeys[root.argA]
    monkeyB = monkeys[root.argB]
    if monkeyB.eval(monkeys) == "unk":
        monkeyA,monkeyB = monkeyB,monkeyA

    print(monkeyA.eval(monkeys), monkeyB.eval(monkeys))
    monkeyA.force(monkeyB.eval(monkeys), monkeys)
    
    humn = monkeys["humn"]
    print(f"{humn.n = }")

# day21b(test21)
day21b(inputs21)