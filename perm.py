import sys

num = int(sys.stdin.read())

if (num == 1):
    print(1)
if (num == 2 or num == 3):
    print("NO SOLUTION")
else:
    first_half = range(1, num // 2 + 1)
    second_half = range(num // 2 + 1, num + 1)

    res = []
    for i in range(0, num // 2):
        res.append(second_half[i])
        res.append(first_half[i])
    if (num % 2 == 1):
        res.append(second_half[-1])

    print(" ".join([str(r) for r in res]))
