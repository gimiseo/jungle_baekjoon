import sys
input = sys.stdin.readline

import heapq

n = int(input())
data = []
ans = []
heapq.heapify(data)
for _ in range(n):
    num = int(input())
    if num == 0:
        if data:
            ans.append(-heapq.heappop(data))
        else:
            ans.append(0)
    heapq.heappush(data, -num)
print("\n".join(map(str,ans)))