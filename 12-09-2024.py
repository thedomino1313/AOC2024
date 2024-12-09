from utils import *

## part 1
with open("inputs/1209.txt", 'r') as f:
	line = list(f.read().strip())
rep = []
for i in range(0, len(line), 2):
	rep += [i//2] * int(line[i])
	if i+1 != len(line):
		rep += ["."] * int(line[i+1])

i,j = 0, len(rep)-1
while i < j:
	if rep[i] == "." and rep[j] != ".":
		rep[i] = rep[j]
		rep[j] = "."
		i+=1
		j-=1
	if rep[j] == ".":
		j-=1
	if rep[i] != ".":
		i+=1

print(sum(x*ind for ind, x in enumerate(rep[:i])))


## part 2
newrep = [("." if i%2 else i//2, int(x)) for i,x in enumerate(line)]
shifts = [x for x in newrep if x[0] != "."][::-1]
for shift in shifts:
	i = newrep.index(shift)
	for j,spot in [(i,x) for i,x in enumerate(newrep[:i]) if x[0] == "."]:
		if spot[1] == shift[1]:
			newrep = newrep[:j] + [shift] + newrep[j+1:i] + [(".", shift[1])] + newrep[i+1:]
			break
		elif spot[1] > shift[1]:
			newrep = newrep[:j] + [shift] + [(spot[0], spot[1] - shift[1])] + newrep[j+1:i] + [(".", shift[1])] + newrep[i+1:]
			break

finalrep = reduce(lambda x,y: x + [y[0]]*y[1], newrep, [])
print(sum(x*ind for ind, x in enumerate(finalrep) if x != "."))