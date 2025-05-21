from math import *

def parse_clusters(task):
    file = open(
        {'A': '../rc/27A.txt',
         'B': '../rc/27B.txt'}
        [task])

    lines = file.readlines()
    points = [
        [float(s.replace('\n', '')) for s in line.split(' ')]
        for line in lines
    ]

    clusters = [[] for _ in range({'A': 3, 'B': 5}[task])]

    if task == 'A':
        for point in points:
            idx = -1
            if point[0] < 4 and point[1] < 4:
                idx = 0
            elif point[0] < 4.5:
                idx = 1
            else:
                idx = 2
            clusters[idx].append(point)
    elif task == 'B':
        for point in points:
            idx = -1
            if point[0] < -0.5 and point[1] < -1:
                idx = 0
            elif point[0] > -0.5 and point[1] < -2:
                idx = 1
            elif point[0] < -1.5 and point[1] > 0:
                idx = 2
            elif point[1] > 3.8:
                idx = 3
            else:
                idx = 4
            clusters[idx].append(point)

    return clusters

def find_experimental_point(cluster):
    max_neighbours_count = -inf
    result_idx = -1

    for cand_idx in range(len(cluster)):
        neighbours = [p for p in cluster if dist(p, cluster[cand_idx]) <= 1.0]
        if len(neighbours) >= max_neighbours_count:
            if len(neighbours) == max_neighbours_count:
                if result_idx != -1 and cluster[result_idx][0] > cluster[cand_idx][0]:
                    continue
            result_idx, max_neighbours_count = cand_idx, len(neighbours)

    return result_idx

def solve(clusters):
    exp_points = []
    for cluster in clusters:
        exp_point_idx = find_experimental_point(cluster)
        exp_points.append(cluster[exp_point_idx])

    answer = inf

    for a in range(len(exp_points)):
        for b in range(a + 1, len(exp_points)):
            answer = min(answer, dist(exp_points[a], exp_points[b]))

    return answer

if __name__ == '__main__':
    for task in ('A', 'B'):
        clusters = parse_clusters(task)
        answer = solve(clusters)
        print(task, int(answer * 10000))

# Answer: 54315 48298