import sys
from collections import Counter

letters = sys.stdin.read().strip()

letter_set = set(letters)
letter_count = Counter(letters)

odd_letters = [l for l in letter_set if letter_count[l] % 2 == 1]

if len(odd_letters) > 1:
    print("NO SOLUTION")
else:
    output = []
    if (odd_letters):
        output.append(odd_letters[0] * letter_count[odd_letters[0]])
    for letter in letter_set:
        if (letter not in odd_letters):
            output.insert(0, letter * (letter_count[letter]//2))
            output.append(letter * (letter_count[letter]//2))
    print("".join(output))
