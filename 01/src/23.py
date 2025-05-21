def transform(origin, target, divided):
    if origin >= 3 * 2 * target:
        return 0

    if origin == target:
        return 1

    return (transform(origin + 3, target, divided) +
            transform(origin * 2, target, divided) +
            (transform(origin // 3, target, True) if not divided else 0))

def solve():
    return transform(6, 25, False)

if __name__ == '__main__':
    answer = solve()
    print(answer)

# Answer: 180