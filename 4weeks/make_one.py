import sys
sys.setrecursionlimit(10000000)

def make_one(n):
    if dp[n] != -1:
        return dp[n]
    if n == 1:
        return 0
    res = make_one(n - 1) + 1
    
    if n % 2 == 0:
        res = min(res, make_one(n // 2) + 1)
    if n % 3 == 0:
        res = min(res, make_one(n // 3) + 1)
    
    dp[n] = res
    return res

n = int(input())
dp = [-1] * (n + 1)
result = make_one(n)
print(result)
