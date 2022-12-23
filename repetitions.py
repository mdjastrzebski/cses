import sys

input = sys.stdin.read()

cur_char = None
cur_length = 0
max_length = 0
for char in input:
    if char == cur_char:
        cur_length += 1
    else:
        cur_char = char
        cur_length = 1

    if cur_length > max_length:
        max_length = cur_length

print(max_length)
