# 바이러스
## BFS
"""
큐(방문 예정지)
방문지 visited = set()

방문과 탐색
- 방문: popleft() -> v.add()
- 탐색: 반복문, 인접 리스트(내가 방문한 곳)
    - 방문하지 않았다면, q.append()
    - 큐 부분에 있는 방문 부분 진행.
"""
from collections import deque

# 인접 리스트 + BFS
V = int(input())
E = int(input())

# 인접행렬
graph = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
adj = [[] for _ in range(V + 1)]

# 셋팅
queue = deque([1])
visited = set()  # 중복 제거, 탐색 빠름.

while queue:
    # 방문
    cur = queue.popleft()
    visited.add(cur)

    # 탐색
    for nxt in range(1, V + 1):
        if adj[cur][nxt] and next not in visited:
            queue.append(nxt)


print(len(visited) - 1)
