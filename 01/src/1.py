from itertools import *

graph = ['38', '679', '179', '56', '489', '249', '23', '159', '23568']
edges = ['AB', 'BV', 'VE', 'EK', 'KI', 'IJ', 'JG', 'GA', 'AD', 'JD', 'DI', 'DE', 'DB']

for p in permutations('ABVGDEJIK'):
    if all(str(p.index(u) + 1) in graph[p.index(v)] for u, v in edges):
        print(*p)

# Answer: 8