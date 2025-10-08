n = int(input())
stairs = [0]
dp = [0] * (n+1)
for _ in range(n):
    stairs.append(int(input()))


#점화식. 화악실히 가져와도 되는 지점. 2칸 전 dp, 3칸전 dp
if n == 1:
    print(stairs[1])
    exit()
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]

for i in range(3,n+1):
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

print(dp[n])

