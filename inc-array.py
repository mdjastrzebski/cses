import sys

lines = sys.stdin.read().split("\n")
count = int(lines[0])
nums = [int(x) for x in lines[1].split(" ")]

prev = 0
result = 0
for num in nums:
    if prev > num:
        result += prev - num
    else:
        prev = num

print(result)
