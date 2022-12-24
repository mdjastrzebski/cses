import sys

num = int(sys.stdin.read())


def get_knights_count(n):
    if n <= 2:
        return 0
    corners = 4 * 2
    next_to_corners = 8 * 3
    external_sides = (n - 4) * 4 * 4
    internal_corners = 4 * 4
    internal_sides = (n - 4) * 4 * 6
    internal = (n - 4)*(n - 4)*8
    return (corners + next_to_corners + internal_corners + external_sides + internal_sides + internal) // 2


for n in range(1, num + 1):
    total = n*n * (n*n - 1) // 2
    invalid = get_knights_count(n)
    print(total - invalid)
