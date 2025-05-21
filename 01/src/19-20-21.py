from math import *

cache = {}

min_heap_size = 32
max_heap_size = 1500

def game(heap):
    if heap < min_heap_size:
        return 0

    result = cache.get(heap, None)
    if result is not None:
        return result

    moves = [heap - k for k in range(1, min_heap_size - 1) if heap % k == 0]

    move_results = list(map(game, moves))
    move_results.sort()

    child_lose_moves = [h for h in move_results if h <= 0]
    child_win_moves = [h for h in move_results if h > 0]

    if child_lose_moves:
        best_child_lose = max(child_lose_moves)
        result = abs(best_child_lose) + 1
    else:
        worst_child_win = max(child_win_moves)
        result = -(worst_child_win + 1)

    cache[heap] = result
    return result

def solve_19():
    answer = -inf

    for start in range(min_heap_size, max_heap_size):
        result = game(start)
        if result == -2:
            answer = max(answer, start)

    return answer

def solve_20():
    answer = [+inf, -inf]

    for start in range(min_heap_size, max_heap_size):
        result = game(start)
        if result == 3:
            answer[0] = min(answer[0], start)
            answer[1] = max(answer[1], start)

    return answer

def solve_21():
    answer = -inf

    for start in range(min_heap_size, max_heap_size):
        result = game(start)
        if result == -4:
            answer = max(answer, start)

    return answer

def solve(task):
    return {'19': solve_19, '20': solve_20, '21': solve_21}[task]()

if __name__ == '__main__':
    for task in ('19', '20', '21'):
        answer = solve(task)
        print(task, answer)

# Answers:
# 19: 61
# 20: 62, 76
# 21: 69