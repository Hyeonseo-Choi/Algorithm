n = int(input())

stack = []
num = 1
result = True
answer = []

for _ in range(n):
    a = int(input())
    if num <= a:
        while num <= a:
            stack.append(num)
            answer.append("+")
            num += 1
        stack.pop()
        answer.append("-")
    else:
        top = stack.pop()
        if top > a:
            print("NO")
            result = False
            break
        else:
            answer.append("-")

if result:
    for i in answer:
        print(i)
