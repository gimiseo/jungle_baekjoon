n, k = map(int, input().split())

items = [(0,0)]

dp = [[0] * (k+1) for _ in range(n + 1)]

for _ in range(n):
    w,v = map(int, input().split())
    items.append((w,v))

for i in range(1, n + 1):
    cur_w, cur_v = items[i]
    for j in range(1, k + 1):
        if dp[i-1][j] != 0:
            dp[i][j] = max(dp[i-1][j], dp[i][j])
        if j == cur_w:
            dp[i][j] = max(cur_v, dp[i][j])
        if dp[i][j] != 0 and (j + cur_w) <= k:
            dp[i][j + cur_w] = max(dp[i][j] + cur_v, dp[i - 1][j + cur_w])

print(max(dp[n]))