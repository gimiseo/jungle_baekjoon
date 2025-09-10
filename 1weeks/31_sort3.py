import sys

input = sys.stdin.readline
n = int(input())
g = {}
for i in range(n):
    num = int(input())
    if not num in g.keys():
        g[num] = 1
    else:
        g[num] += 1
for i in sorted(g.keys()):
    for j in range(g[i]):
        print(i)