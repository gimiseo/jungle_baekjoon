n, k = map(int, input().split())

items = [(0,0)]

dp = [[0] * (k+1) for _ in range(n + 1)]

for _ in range(n):
    w,v = map(int, input().split())
    items.append((w,v))

#그순간에서의 최대 해를 찾아낸다.
for i in range(1, n + 1):
    cur_w, cur_v = items[i]
    for j in range(1, k + 1):
        if j >= cur_w:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - cur_w] + cur_v)
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[n][k])