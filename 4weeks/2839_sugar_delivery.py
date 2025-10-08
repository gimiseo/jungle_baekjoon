import sys
sys.setrecursionlimit(1_000_000)
def sugar(N):
    # 기저 조건
    if N == 0:
        return 0
    if N < 0:
        return float('inf')
    #이미 있으면 반환
    if dp_t[N] != -1:
        return dp_t[N]
    # 3kg, 5kg 빼고 재귀 호출
    min_value = min(sugar(N - 3), sugar(N-5)) + 1
    dp_t[N] = min_value
    # -1 처리 (불가능한 경우 거르기)
    return (dp_t[N])

n = int(input())
dp_t = [-1] * (n + 1)
answer = sugar(n)
if answer == float('inf'):
    answer = -1
print(answer)