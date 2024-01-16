from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdin.readline
pQue = PriorityQueue()

n = int(input())

for _ in range(n):
    x = int(input())
    if x == 0:
        if pQue.empty():
            print("0\n")
        else:
            print(str(pQue.get()[1])+"\n")
    else:
        pQue.put((abs(x), x))