import math
import sys
from collections import Counter

lines = sys.stdin.read().split('\n')
letters = Counter(sorted(lines[0]))


def count(letters):
    res = math.factorial(letters.total())
    for letter in letters:
        res //= math.factorial(letters[letter])
    return res


def gen(str, letters):
    for letter in letters:
        if letters[letter] <= 0:
            continue

        newStr = str + letter
        newCounter = Counter(letters)
        newCounter[letter] -= 1

        if newCounter.total():
            gen(newStr, newCounter)
        else:
            print(newStr)


print(count(letters))
gen("", letters)
