def parse_input():
    file = open('../rc/09.txt')
    string_lines = file.readlines()
    lines = [list(map(int, line.split('\t'))) for line in string_lines]
    return lines

def solve(lines):
    answer = 0

    for line in lines:
        even = [number for number in line if number % 2 == 0]
        odd = [number for number in line if number % 2 == 1]

        if all(even.count(number) < 2 for number in even):
            continue

        if all(odd.count(number) < 2 for number in odd):
            continue

        if all(even.count(number) > 1 for number in even):
            continue

        if all(odd.count(number) > 1 for number in odd):
            continue

        if sum(even) <= sum(odd):
            continue

        answer += 1

    return answer

if __name__ == '__main__':
    lines = parse_input()
    answer = solve(lines)
    print(answer)

# Answer: 38