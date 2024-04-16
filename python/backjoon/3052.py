# 나머지
arr = [int(input()) for _ in range(10)]
tmp = set()

for i in arr:
    n = i % 42
    tmp.add(n)


print(len(tmp))
