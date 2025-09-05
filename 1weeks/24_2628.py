#꽤어렵네.. 자르고 버린다?-> 버린게 제일 클수있음
#이거 수식 써야됨
#수식 ... 최대가로구간x최대세로구간이 최대 넒이임..ㅋㅋㅋ
x, y = map(int, input().split())
x_list = []
y_list = []
num = int(input())
for _ in range(num):
    dir, start = map(int, input().split())
    if dir == 0:
        y_list.append(start)
    elif dir == 1:
        x_list.append(start)
x_list.append(x)
y_list.append(y)
x_list.sort()
y_list.sort()
curr_x = 0
curr_y = 0
max_width = 0
max_height = 0
for n in x_list:
    if max_width < n - curr_x:
        max_width = n - curr_x
    curr_x = n
for m in y_list:
    if max_height < m - curr_y:
        max_height = m - curr_y
    curr_y = m
print(max_width*max_height)
