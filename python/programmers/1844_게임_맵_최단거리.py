from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


def solution(maps):
    queue = deque([(1, 0, 0)])
    visited = set([(0, 0)])
    n, m = len(maps), len(maps[0])
    answer = -1

    while queue:
        cnt, r, c = queue.popleft()

        if r == n - 1 and c == m - 1:
            answer = cnt
            break

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            if (
                0 <= nr < n
                and 0 <= nc < m
                and (nr, nc) not in visited
                and maps[nr][nc] != 0
            ):
                continue
            queue.append((cnt + 1, nr, nc))
            visited.add((nr, nc))

    return answer


solution(
    [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1],
    ]
)
