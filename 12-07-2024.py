from utils import *

def solve(result, nums, part2 = False):
	if len(nums) == 1:
		if nums[0] == result:
			return 1
		return 0
	return solve(result, [nums[0]*nums[1]]+nums[2:]) + solve(result, [nums[0]+nums[1]]+nums[2:])

## part 1
with open(FILENAME, 'r') as f:
	problems = [(int(x[0]), list(map(int, x[1].split()))) for x in map(lambda x: x.split(": "), f)]
print(sum(problem[0] for problem in problems if solve(*problem)))

## part 2
def solve(result, nums):
	if len(nums) == 1:
		if nums[0] == result:
			return 1
		return 0
	return solve(result, [nums[0]*nums[1]]+nums[2:]) + solve(result, [nums[0]+nums[1]]+nums[2:]) + solve(result, [int(str(nums[0])+str(nums[1]))]+nums[2:])

print(sum(problem[0] for problem in problems if solve(*problem)))