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
        if args.isdigit():
            self.n = int(args)
        else:
            self.argA, self.op, self.argB = args.split(" ")
            if self.op == "/":
                self.op = "//"

            self.n = None

    def eval(self, monkeys):
        if self.n == None:        
            a = monkeys[self.argA].eval(monkeys)
            b = monkeys[self.argB].eval(monkeys)
            self.n = eval(f"{a} {self.op} {b}")
        return self.n

def day21(lines):
    monkeys = {}
    for line in lines.split("\n"):
        monkey = Monkey(line)
        monkeys[monkey.name] = monkey

    root = monkeys["root"]
    print(f"{root.eval(monkeys) = }")

# day21(test21)
day21(inputs21)