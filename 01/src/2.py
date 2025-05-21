from itertools import *

args = 'wxyz'

def f(w, x, y, z):
    return x and (z <= y) or w and (x <= (not z))

for a in product([0, 1], repeat = 6):
    table = (
        (a[0], 1, 1, a[1]),
        (a[2], 1, a[3], a[4]),
        (1, 1, 1, a[5])
    )

    if len(table) != len(set(table)):
        continue

    for p in permutations(args):
        if all(
            f(*[line[p.index(c)] for c in args]) == 0
            for line in table
        ):
            print(*p)

# Answer: wzxy