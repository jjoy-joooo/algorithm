import sys

input = sys.stdin.readline


def DFS(now):
    visited.add(now)

    for after in adj[now]:
        if after not in visited:
            DFS(after)


V = int(input())
E = int(input())


# 인접리스트 구조화
adj = [[] for _ in range(V + 1)]
visited = set()
