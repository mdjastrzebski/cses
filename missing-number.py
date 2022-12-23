import sys

lines = sys.stdin.read().split("\n")
count = int(lines[0])
nums = [int(x) for x in lines[1].split(" ")]

all = set(range(1, count + 1))
for num in nums:
    all.remove(num)

print(all.pop())
