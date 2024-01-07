checkList = [0] * 4
currentList = [0] * 4
checkCount = 0

def dnaAdd(c):
    global checkList, currentList, checkCount
    if c == 'A':
        currentList[0] += 1
        if currentList[0] == checkList[0]:
            checkCount += 1
    elif c == 'C':
        currentList[1] += 1
        if currentList[1] == checkList[1]:
            checkCount += 1
    elif c == 'G':
        currentList[2] += 1
        if currentList[2] == checkList[2]:
            checkCount += 1
    elif c == 'T':
        currentList[3] += 1  
        if currentList[3] == checkList[3]:
            checkCount += 1
              
    
def dnaRemove(c):
    global checkList, currentList, checkCount
    if c == 'A':
        if currentList[0] == checkList[0]:
            checkCount -= 1
        currentList[0] -= 1
    elif c == 'C':
        if currentList[1] == checkList[1]:
            checkCount -= 1
        currentList[1] -= 1
    elif c == 'G':
        if currentList[2] == checkList[2]:
            checkCount -= 1
        currentList[2] -= 1
    elif c == 'T':
        if currentList[3] == checkList[3]:
            checkCount -= 1
        currentList[3] -= 1

def dnaChange(i, n):
    global checkList, currentList, checkCount
    currentList[i] += n
    if currentList[i] == checkList[i]:
        checkCount += n

s, p = map(int, input().split())
result = 0
tempDnaList = list(input())
checkList = list(map(int, input().split()))

for i in range(4):
    if (checkList[i] == 0):
        checkCount += 1

for i in range(p):
    dnaAdd(tempDnaList[i])

if checkCount == 4:
    result += 1

for i in range(p, s):
    j = i - p
    dnaAdd(tempDnaList[i])
    dnaRemove(tempDnaList[j])
    if checkCount == 4:
        result += 1

print(result)