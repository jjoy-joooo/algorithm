# 베스트샐러
N = int(input())
arr = [input() for _ in range(N)]
tmp = {}


for book in arr:
    if tmp.get(book, -1) == -1:
        tmp[book] = 0

    tmp[book] += 1

sorted = sorted(tmp.items(), key=lambda x: (-x[1], x[0]))

print(sorted[0][0])
