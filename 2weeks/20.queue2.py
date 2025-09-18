import sys
from collections import deque

input = sys.stdin.readline

queue = deque([])

resultlist = []

num = int(input())
for _ in range(num):
    order = (input().rstrip().split())
    if order[0] == "push":
        queue.append(int(order[1]))
    elif order[0] == "pop":
        if queue:
            resultlist.append(queue.popleft())
        else:
            resultlist.append(-1)
    elif order[0] == "size":
        resultlist.append(len(queue))
    elif order[0] == "empty":
        if queue:
            resultlist.append(0)
        else:
            resultlist.append(1)
    elif order[0] == "front":
        if queue:
            resultlist.append(queue[0])
        else:
            resultlist.append(-1)
    elif order[0] == "back":
        if queue:
            resultlist.append(queue[-1])
        else:
            resultlist.append(-1)
for word in resultlist:
    print(word)