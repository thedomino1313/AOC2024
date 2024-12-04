from functools import *
from collections import Counter

## part 1
with open("input1201.txt", "r") as f:
    print(sum(map(lambda x: abs(x[0]-x[1]), zip(*map(sorted, zip(*(map(int, x.split()) for x in f)))))))

#part 2
with open("input1201.txt", "r") as f:
    input = list(zip(*[map(int, x.split()) for x in f]))

c = Counter(input[1])

print(sum(map(lambda x: x * c[x], input[0])))