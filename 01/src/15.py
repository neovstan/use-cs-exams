def div(n, m):
    return n % m == 0

def f(x, A):
    return (not div(x, 34) or not div(x, 122)) <= (not div(x, A))

def solve():
    for A in range(1, 10000):
        if all(f(x, A) for x in range(1, 10000)):
            return A
    return -1

if __name__ == '__main__':
    answer = solve()
    print(answer)

# Answer: 2074