# 미로
# import sys

# input = sys.stdin.readline

"""
Q = [(0, 0)] # 시작 좌표
S = (r, c)
DFS = (r, c)

출발 좌표 찾고, 셋팅 Q 또는 S 또는 DFS에 넣고 시작

1. 구조화
2. 세팅
3. 방문
4. 탐색
"""

from collections import deque

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

for tn in range(T):
    N = int(input())

    maze = [list(map(int, input())) for _ in range(N)]

    queue = deque()
    visited = set()
    ans = 0

    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:  # 출발지 찾기
                queue.append((-1, r, c))

    """ 델타탐색
    1. 범위
    2. 방문 x
    3. 벽 x
    
    방문 표시 - 찾았는가?
    """
    while queue:
        # 방문
        cur, r, c = queue.popleft()

        print("======================== ", r, c)
        visited.add((r, c))

        if maze[r][c] == 3:
            ans = 1
            break

        # 탐색
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            # 범위에 조건
            if (
                0 <= nr < N
                and 0 <= nc < N
                and (nr, nc) is not visited
                and maze[nr][nc] != 1
            ):
                ans += 1
                queue.append((cur + 1, nr, nc))

    result = tn + 1
    print("======================== 1 ", queue)
    print("======================== 2 ", visited)
    print("#", result, ans)
