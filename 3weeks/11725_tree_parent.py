from collections import deque

n, k = map(int, input().split())

coin_used = [-1] * (k + 1)
coin_used[0] = 0
coins = []
for _ in range(n):
    coins.append(int(input()))

q = deque()
q.append(0)

while q:
    cur = q.popleft()
    for c in coins:
        nex = cur + c
        if nex <= k and coin_used[nex] == -1:
            coin_used[nex] = coin_used[cur] + 1
            q.append(nex)
print(coin_used[k])