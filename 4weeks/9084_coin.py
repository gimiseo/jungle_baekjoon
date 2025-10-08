T = int(input())

result = []

for _ in range(T):
    n = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    dp = [0] * (M+1)

    #만약 목표 금액이 1이라고 했을
    dp[0] = 1
    for coin in coins:
        for j in range(coin, M+1):
            dp[j] += dp[j - coin]
    result.append(dp[M])

for a in result:
    print(a)
    