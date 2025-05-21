from bisect import *
from math import *

def parse_input():
    file = open('../rc/24.txt')
    return file.read()

def solve(s):
    n = len(s)

    pref_count = [0] * (n + 1)
    suff_count = [0] * (n + 1)

    for pref in range(1, n + 1):
        pref_count[pref] = pref_count[pref - 1]

        if pref < 2:
            continue

        if s[pref-2:pref] == 'AB':
            pref_count[pref] += 1

    for suff in range(n - 1, -1, -1):
        suff_count[suff] = suff_count[suff + 1]

        if suff > n - 2:
            continue

        if s[suff:suff+2] == 'CD':
            suff_count[suff] += 1

    answer = -inf

    for right in range(1, n + 1):
        i1 = bisect_right(pref_count, pref_count[right] - 30, 0, right) - 1
        i2 = bisect_left(suff_count_neg, suff_count_neg[right - 1] - 200, 0, right)

        if i2 > i1:
            continue

        answer = max(answer, right - i2)

    return answer

if __name__ == '__main__':
    s = parse_input()
    answer = solve(s)
    print(answer)

# Answer: 2511