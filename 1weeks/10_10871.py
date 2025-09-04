a, b = map(int, input().split())
num_list = list(map(int, input().split()))

result_list = []
for i in num_list:
    if i < b:
        result_list.append(i)

print(*result_list)