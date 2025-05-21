def parse_input():
    file = open('../rc/17.txt')
    lines = file.readlines()
    numbers = list(map(int, lines))
    return numbers

def last_digit(number):
    return number % 10

def solve(numbers):
    triples_count, max_triple_sum = 0, 0
    min_number, max_number = min(numbers), max(numbers)

    for first in range(len(numbers) - 2):
        triple = [numbers[i] for i in (first, first + 1, first + 2)]
        max_triple_number = max(triple)
        triple_last_digits = list(map(last_digit, triple))

        if len(set(triple_last_digits)) == 3:
            continue

        if last_digit(max_triple_number) != last_digit(max_number):
            continue

        if any(last_digit(number) == last_digit(min_number) for number in triple):
            continue

        triples_count += 1
        max_triple_sum = max(max_triple_sum, sum(triple))

    return triples_count, max_triple_sum

if __name__ == '__main__':
    numbers = parse_input()
    answer = solve(numbers)
    print(answer)

# Answer: 244, 262362