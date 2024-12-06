from utils import *

with open(FILENAME, 'r') as f:
	rules_, instructions_ = [x.split() for x in f.read().split("\n\n")]
rules = defaultdict(list)
for left,right in map(lambda x: x.split("|"), rules_):
	rules[right].append(left)
instructions = list(map(lambda x: x.split(","), instructions_))

## part 1
print(sum(int(instruction[(len(instruction)-1)//2]) for instruction in instructions if not any(j in rules[instruction[i]] for i in range(len(instruction)) for j in instruction[i+1:])))

## part 2
wrong = (instruction for instruction in instructions if any(j in rules[instruction[i]] for i in range(len(instruction)) for j in instruction[i+1:]))

total = 0
for instruction in wrong:
	for i in range(len(instruction)):
		for j in range(i+1, len(instruction)):
			if instruction[j] in rules[instruction[i]]:
				instruction[i],instruction[j]=instruction[j],instruction[i]
	total += int(instruction[(len(instruction)-1)//2])

print(total)