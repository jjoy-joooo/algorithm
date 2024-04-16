import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]
tmp = {}

for i in arr:
    key = i[0]
    val = i[1]
    if tmp.get(key, -1) == -1:
        tmp[key] = []

    tmp[key].append(val)

for i in sorted(tmp)[::-1]:
    if len(tmp[i]) % 2 == 1:
        print(i)
