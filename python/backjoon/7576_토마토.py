import sys

input = sys.stdin.readline

from collections import deque

"""
1. 세팅 -> 출발점 찾기
2. 방문
3. 탐색
4. 후처리
    - 다 있었는지?
    - 다 익었다면 최댓값
"""

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

queue = deque()

for r in range(N):
    for c in range(M):
        if box[r][c] == 1:
            queue.append((r, c))

# BFS
while queue:
    r, c = queue.popleft()

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]

        if 0 <= nr and 0 <= nc < M and box[nr][nc] == 0:
            queue.append((nr, nc))
            # 방문 표시
            box[nr][nc] = box[r][c] + 1

ans = -1
for line in box:
    for t in line:
        if t == 0:
            print(-1)
            exit(0)
        else:
            ans = max(ans, t)

print(ans - 1)
