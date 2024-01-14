n = int(input())
a = list(map(int, input().split()))
answer = [-1]*n
stack = []
result = ""

for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        answer[stack.pop()] = a[i]
    stack.append(i)

print(*answer)
