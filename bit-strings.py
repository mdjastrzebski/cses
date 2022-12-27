import sys
n = int(sys.stdin.read())

res = 1
base = 2
while n:
    if n % 2:
        res = (res * base) % 1_000_000_007

    n //= 2
    base = (base*base) % 1_000_000_007

print(res)
