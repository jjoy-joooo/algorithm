V = int(input())  # 정점
E = int(input())  # 간선

adj = [[] for _ in range(V + 1)]
for _ in range(E):
    r, c = map(int, input().split())
    adj[r].append(c)
    adj[c].append(r)

print(adj)
