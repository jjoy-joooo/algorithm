V = int(input())  # 정점
E = int(input())  # 간선

result = []
# 빈판 만들기
adj = [[0] * (V + 1) for _ in range(V + 1)]
for i in range(V):
    tmp = []
    for _ in range(V):
        tmp.append(0)

    result.append(tmp)

print(result)

# 간선 정보 입력받기
arr = [list(map(int, input().split())) for _ in range(E)]

for i in arr:
    r, c = i
    result[r][c] = 1
    result[c][r] = 1

print(result)
