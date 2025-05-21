from fnmatch import *

def prime_numbers(n):
    result = []
    is_prime = [True] * n

    for a in range(2, n):
        if is_prime[a]:
            result.append(a)
            for k in range(2 * a, n, a):
                is_prime[k] = False

    return result

def solve():
    answer = []

    for p in prime_numbers(10 ** 6):
        cand = p ** 4

        if cand > 2 * (10 ** 9):
            break

        if fnmatch(str(cand), '1*7*1'):
            answer.append(cand)

    return answer

if __name__ == '__main__':
    answer = solve()
    print(answer)

# Answer: 1874161, 12117361, 131079601, 163047361, 1073283121, 1387488001