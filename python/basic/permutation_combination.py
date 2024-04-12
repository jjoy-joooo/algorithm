# 순열 조합
from itertools import combinations, permutations

arr = ["a", "b", "c"]
combi = list(combinations(arr, 2))
permu = list(permutations(arr, 3))

print(combi)
print(permu)
