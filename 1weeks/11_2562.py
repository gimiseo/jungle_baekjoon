list = []
for _ in range(9):
    a = int(input())
    list.append(a)

max_num = 0
max_index = 0
for i in range(9):
    if max_num < list[i]:
        max_num = list[i]
        max_index = i
print(max_num)
print(max_index + 1)