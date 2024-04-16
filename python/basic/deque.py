from collections import deque

queue = deque()  # deque([5, 6, 3])
queue.append(5)
queue.append(6)
queue.append(3)

print(queue)

a = queue.popleft()
print(a)
