from collections import deque
que = deque()
n = int(input())

for i in range(1, n+1):
    que.append(i)

while len(que) > 1:
    que.popleft()
    que.append(que.popleft())

print(que.popleft())
