from utils import *

## part 1
with open("inputs/1206.txt", 'r') as f:
	map_ = f.read().split("\n")

initi = 0
initj = 0
while True:
	if (initj := map_[initi].find("^")) != -1:
		break
	else:
		initi+=1

spots = set()
map_ = [list(x) for x in map_]
directions = [(-1,0),(0,1),(1,0),(0,-1)]
dirIndex = 0
spaces = set()
v = set()
i,j = initi,initj


while i not in (0,len(map_)-1) and j not in (0,len(map_[0])-1):
	direction = directions[dirIndex]
	if map_[(newi := i+direction[0])][(newj := j+direction[1])] == "#":
		dirIndex = (dirIndex+1)%4
	else:
		spaces.add((i,j))
		i,j = newi,newj

spaces.add((i,j))
print(len(spaces))

# part 2
spots = set()
directions = [(-1,0),(0,1),(1,0),(0,-1)]
for x,y in spaces:
	if map_[x][y] != "#":
		visited = set()
		dirIndex = 0
		i,j = initi,initj
		map_[x][y] = "#"
		while i not in (0,len(map_)-1) and j not in (0,len(map_[0])-1):
			direction = directions[dirIndex]
			if (i,j,dirIndex) in visited:
				spots.add((x,y))
				break
			if map_[(newi := i+direction[0])][(newj := j+direction[1])] == "#":
				dirIndex = (dirIndex+1)%4
			else:
				visited.add((i,j,dirIndex))
				i,j = newi,newj
		map_[x][y] = "."

print(len(spots))