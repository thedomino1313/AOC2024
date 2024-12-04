from utils import *

# part 1
with open(FILENAME, 'r') as f:
    print(sum([all([-4 < (x[i] - x[i-1]) < 0 for i in range(1, len(x))]) or all([0 < (x[i] - x[i-1]) < 4 for i in range(1, len(x))]) for x in map(lambda x: [int(y) for y in x.split()], f)]))

# part 2
with open(FILENAME, 'r') as f:
    print(sum([any([all([-4 < (x[i] - x[i-1]) < 0 for i in range(1, len(x))]) or all([0 < (x[i] - x[i-1]) < 4 for i in range(1, len(x))]) for x in y]) for y in [[z[:i] + z[i+1:] for i in range(len(z))] for z in map(lambda x: [int(y) for y in x.split()], f)]]))
