import sys
input = sys.stdin.readline

num = int(input())
stack = []
for _ in range(num):
    tempNum = int(input().split()[0])
    if tempNum == 0:
        stack.pop()
    else:
        stack.append(tempNum)
print(sum(stack))