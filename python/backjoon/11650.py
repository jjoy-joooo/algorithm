# 좌표 정렬하기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort()
for i in arr:
    print(*i)
