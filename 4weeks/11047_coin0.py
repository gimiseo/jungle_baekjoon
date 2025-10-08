N, K = map(int, input().split())
coin_list = []
for _ in range(N):
    coin_list.append(int(input()))

#greedy start
count = 0
for coin in reversed(coin_list):
    if K < coin:
        continue
    else:
        count += (K//coin)
        K = K % coin

print(count)