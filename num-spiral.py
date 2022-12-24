import sys

lines = sys.stdin.read().split("\n")
count = int(lines[0])


def get_spiral_num(x, y):
    side = max(x, y)
    start_num = (side - 1) * (side - 1) + 1
    end_num = side * side

    # clockwise
    if side % 2 == 1:
        if y == side:
            return start_num + x - 1
        else:
            return end_num - y + 1
    # counter-clockwise
    else:
        if x == side:
            return start_num + y - 1
        else:
            return end_num - x + 1


for count in range(1, count + 1):
    line = lines[count]
    tokens = line.split(" ")
    y = int(tokens[0])
    x = int(tokens[1])
    print(get_spiral_num(x, y))
