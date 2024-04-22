# 바이러스
## DFS
from collections import deque

# 인접 리스트 + BFS
V = int(input())
E = int(input())

# 인접행렬 구조화
# graph = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
adj = [[0] * (V + 1) for _ in range(V + 1)]

for u in range(E):
    

# 셋팅
# queue = deque([1])
# visited = set()  # 중복 제거, 탐색 빠름.


# while queue:
#     # 방문
#     cur = queue.popleft()
#     visited.add(cur)

#     # 탐색

#     for nxt in adj[cur]:
#         # 리스트로하면 시간 초과기때문에, 집합 자료 구조로 해야 함...!
#         if nxt in visited:
#             continue
#         queue.append(nxt)


print(len(visited) - 1)
