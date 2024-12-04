from functools import *
from collections import Counter
import regex as re

## part 1
with open("input1203.txt", "r") as f:
    print(sum([int(x.group(1)) * int(x.group(2)) for x in re.compile(r"mul\(([0-9]*),([0-9]*)\)").finditer(f.read())]))

## part 2
with open("input1203.txt", "r") as f:
    print(sum([sum([int(x.group(1)) * int(x.group(2)) for x in re.compile(r"mul\(([0-9]*),([0-9]*)\)").finditer(y.group(1))]) for y in re.compile(r"(?:(?:do\(\))|(?:^))(.*?)(?:(?:don't\(\))|(?:$))", re.S).finditer(f.read())]))