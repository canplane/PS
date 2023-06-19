from itertools import combinations

N, M = map(int, input().split())

combs = list(combinations(range(1, N + 1), M))
for comb in combs:
    print(*comb)