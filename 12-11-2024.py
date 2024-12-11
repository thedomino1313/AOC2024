from utils import *

with open(FILENAME, 'r') as f:
    nums = f.read().strip().split()

@cache
def transform(num):
    if num == "0":
        return ["1"]
    elif not (l := len(num))%2:
        return [str(int(num[:l//2])), str(int(num[l//2:]))]
    else:
        return [str(int(num)*2024)]
@cache
def blink(num, times):
    if times == 0:
        return 1
    else:
        return sum(blink(x, times-1) for x in transform(num))
# part 1
print(sum(blink(x, 25) for x in nums))
# part 2
print(sum(blink(x, 75) for x in nums))
