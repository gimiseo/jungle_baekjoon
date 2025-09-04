a = int(input())
b = int(input())

result = 0
for i in range(3):
    temp = a * (b % 10)
    print(temp)
    b //= 10
    result += (temp * (10 ** i))
print(result)