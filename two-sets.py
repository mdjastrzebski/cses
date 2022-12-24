import sys

num = int(sys.stdin.read())


def get_split(n):
    total = n*(n+1) // 2
    not_used = [*range(1, n+1)]
    used = set()
    remaining = total // 2
    while remaining > 0:
        if remaining <= not_used[-1]:
            not_used.remove(remaining)
            used.add(remaining)
            return (used, not_used)

        last = not_used.pop()
        remaining -= last
        assert remaining > 0, "Remaining should be possitve"
        used.add(last)


if num % 4 == 1 or num % 4 == 2:
    print("NO")
else:
    print("YES")
    (used, not_used) = get_split(num)
    assert sum(used) == sum(not_used)
    print(len(used))
    print(*used)
    print(len(not_used))
    print(*not_used)
