import sys

input = sys.stdin.readline

n = int(input().rstrip())
towers = list(map(int, input().split()))

ans = [0]*n
stack = []

for i, h in enumerate(towers, start= 1):
    while stack and stack[-1][0] <= h:
        stack.pop()
    if stack:
        ans[i - 1] = stack[-1][1]
    else:
         ans[i - 1] = 0
    stack.append((h, i))
print(*ans)