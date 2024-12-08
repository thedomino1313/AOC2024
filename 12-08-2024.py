from utils import *

## part 1
with open(FILENAME, 'r') as f:
	antennas = [list(x.strip()) for x in f]

symbols = {symbol: [(x,y) for x in range(len(antennas)) for y in range(len(antennas[0])) if antennas[x][y] == symbol] for line in antennas for symbol in line if symbol != "."}

print(len(set((new1, new2) for s in symbols for loc1 in symbols[s] for loc2 in symbols[s] if loc1 != loc2 and 0 <= (new1 := loc1[0]-(loc2[0]-loc1[0])) < len(antennas) and 0 <= (new2 := loc1[1]-(loc2[1]-loc1[1])) < len(antennas[0]))))


## part 2
print(len(set((new1, new2) for s in symbols for loc1 in symbols[s] for loc2 in symbols[s] if loc1 != loc2 for slope1,slope2 in [(loc2[0]-loc1[0], loc2[1]-loc1[1])] for new1,new2 in zip((range(loc1[0], len(antennas), slope1) if slope1 > 0 else range(loc1[0], -1, slope1)), (range(loc1[1], len(antennas[0]), slope2) if slope2 > 0 else range(loc1[1], -1, slope2))))))