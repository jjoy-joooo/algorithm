arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
N = 3
r = c = 2  # 시작점

dr = [1, -1, 0, 0]  # 하, 상, 좌, 우
dc = [0, 0, -1, 1]

for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    # if nr < 0 or nr >= N or nc < 0 or nc >= N:
    #     continue
    if 0 <= nr < N and 0 <= nc < N:
        print(arr[nr][nc])
