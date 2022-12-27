import sys

n = int(sys.stdin.read())
i = 5
res = 0
while i <= n:
    res += n // i
    i *= 5

print(res)
