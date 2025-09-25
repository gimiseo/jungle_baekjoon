#인자받기
n = int(input())
num_list = list(map(int, input().split()))
operators = list(map(int, input().split()))

result_list = []

#사칙연산 함수
def elementary_arithmetic(n, a, b):
    if n == 0:
        return a + b
    elif n == 1:
        return a - b
    elif n == 2:
        return a * b
    elif n == 3:
        if a < 0:
            a = -a
            value = a // b
            value = -value
            return value
        return a // b

#dfs
def dfs(result, num):
    if num == n - 1:
        result_list.append(result)
        return
    for i in range(4):
        if operators[i] != 0:
            operators[i] -= 1
            dfs(elementary_arithmetic(i, result, num_list[num+1]), num + 1)
            operators[i] += 1

#최종
dfs(num_list[0], 0)
print(max(result_list))
print(min(result_list))