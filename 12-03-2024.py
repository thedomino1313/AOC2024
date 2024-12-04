from utils import *

## part 1
with open(FILENAME, "r") as f:
    print(sum([int(x.group(1)) * int(x.group(2)) for x in re.compile(r"mul\(([0-9]*),([0-9]*)\)", re.S).finditer(f.read())]))

## part 2
with open(FILENAME, "r") as f:
    print(sum([math.prod(map(int, x.groups())) for y in re.compile(r"(?:(?:do\(\))|(?:^))(.*?)(?:(?:don't\(\))|(?:$))", re.S).finditer(f.read()) for x in re.compile(r"mul\(([0-9]*),([0-9]*)\)").finditer(y.group(1))]))