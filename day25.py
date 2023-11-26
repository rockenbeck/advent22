from advent_2022_inputs import *

import re
from collections import defaultdict

test25="""1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""


def s2d(s):
    n = 0
    for ch in s:
        n *= 5
        if ch == '2':
            n += 2
        elif ch == '1':
            n += 1
        elif ch == '0':
            pass
        elif ch == '-':
            n -= 1
        elif ch == '=':
            n -= 2
        else:
            assert(False)
        
    return n

BS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def to_base(s, b):
    res = ""
    while s:
        res+=BS[s%b]
        s//= b
    return res[::-1] or "0"

def d2s(n):
    if n == 0:
        return "0"
    s5 = to_base(n, 5)
    # return s5
    snafu = ""
    carry = 0
    for ch in s5[::-1]:
        d = int(ch) + carry
        carry = 0
        if d < 3:
            snafu = str(d) + snafu
        elif d == 3:
            snafu = '=' + snafu
            carry = 1
        elif d == 4:
            snafu = '-' + snafu
            carry = 1
        elif d == 5:
            snafu = '0' + snafu
            carry = 1
    if carry:
        snafu = '1' + snafu
    return snafu


# print(s2d("1121-1110-1=0"))
# print(d2s(2022))

def day25(lines):
    sum = 0
    for line in lines.split("\n"):
        sum += s2d(line)
    print(f"{sum = } = {d2s(sum)}")

# day25(test25)
day25(input25)

