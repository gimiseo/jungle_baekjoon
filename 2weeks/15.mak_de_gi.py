n = int(input())
bar_list = []
for _ in range(n):
    bar_list.append(int(input()))

max = 0
count = 0
while bar_list:
    bar = bar_list.pop()
    if max < bar:
        max = bar
        count += 1
print(count)