num = int(input())
list = []
for _ in range(num):
    a, b = map(int, input().split())
    list.append(a+b)
for i in list:
    print(i)