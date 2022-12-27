import sys
lines = sys.stdin.read().split('\n')
num = int(lines[0])

for n in range(1, num + 1):
    a, b = map(int, lines[n].split())
    if (a + b) % 3 == 0 and a >= b // 2 and b >= a // 2:
        print("YES")
    else:
        print("NO")
