# 메모리제이션 첫번째

# 첫번째, 배열을 선언한다.

n = int(input())
memoization = [-1] * (n + 1)

def fibonacci(num):
    if memoization[num] != -1:
        return memoization[num]
    elif num <= 2:
        memoization[num] = 1
    else:
        memoization[num] = fibonacci(num - 1) + fibonacci(num - 2)
    return memoization[num]

print(fibonacci(n))