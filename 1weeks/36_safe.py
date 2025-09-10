# def in_range(x,y):
#     return 0 <= x and x < n and \
#             0 <= y and y < n

# def move_unsafe(x,y):
#     dxs = [0,0,1,-1]
#     dys = [1,-1,0,0]
#     stack = []
#     stack.append((x,y))

#     while stack:
#         new_x, new_y = stack.pop()
#         visited[new_x][new_y] = 1

#         for dx, dy in zip(dxs, dys):
#             next_x, next_y = new_x + dx , new_y + dy
#             if not in_range(next_x,next_y):
#                 continue
#             if safe[next_x][next_y] == 0 and visited[next_x][next_y] != 1:
#                 stack.append((next_x,next_y))
#                 visited[next_x][next_y] = 1
#             if safe[next_x][next_y] == 1 and visited[next_x][next_y] != 1:
#                 count_safe(next_x, next_y)
    

# def count_safe(x,y):
#     global area
#     dxs = [0,0,1,-1]
#     dys = [1,-1,0,0]

#     stack = []
#     pos = []
#     stack.append((x,y))
#     visited[x][y] = 1
#     count = 1

#     while stack:
#         new_x, new_y = stack.pop()

#         for dx, dy in zip(dxs, dys):
#             next_x, next_y = new_x + dx , new_y + dy
#             if not in_range(next_x,next_y):
#                 continue
#             if safe[next_x][next_y] == 1 and visited[next_x][next_y] != 1:
#                 stack.append((next_x,next_y))
#                 visited[next_x][next_y] = 1
#             if safe[next_x][next_y] == 0 and visited[next_x][next_y] != 1:
#                 pos.append((next_x,next_y))
#     area += 1
#     while pos:
#         cur_x, cur_y = pos.pop()
#         if visited[cur_x][cur_y] != 1:
#             move_unsafe(cur_x, cur_y)



# n= int(input())
# grid = [list(map(int, input().split())) for _ in range(n)]

# k = 1
# safe_area = []
# #일단 전부 침수 지역일 경우 까지 돌려야함
# while True:
#     area = 0
#     stop = True
#     safe = [[0 for _ in range(n)] for _ in range(n)]
#     visited = [[0 for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if grid[i][j] > k:
#                 safe[i][j] = 1
#                 stop = False
#     if safe[0][0] == 1:
#         count_safe(0,0)
#     else:
#         move_unsafe(0,0)
#     safe_area.append(area)
#     if stop:
#         break
#     k += 1

# max = 0
# for i in range(len(safe_area)):
#     if safe_area[i] > max:
#         max = safe_area[i]
# if k == 1:
#     print(1)
# else:
#     print(max)

#g선생의 조언 - 따로 만들지마라. safe...를


n= int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
count_list = []

def in_range(x,y):
    return 0 <= x and x < n and \
            0 <= y and y < n

def make_safeArea(h):
    safe = [[0 for _ in range(n)] for _ in range(n)]
    count = 0 

    def dfs(x,y):
        nonlocal safe
        dxs = [0,0,1,-1]
        dys = [1,-1,0,0]
        stack = []
        stack.append((x,y))
        safe[i][j] = 0

        while stack:
            cur_x, cur_y = stack.pop()
            for dx, dy in zip(dxs, dys):
                next_x, next_y = cur_x + dx , cur_y + dy
                if not in_range(next_x,next_y):
                    continue
                if safe[next_x][next_y] == 1:
                    stack.append((next_x,next_y))
                    safe[next_x][next_y] = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j] > h:
                safe[i][j] = 1
    for i in range(n):
        for j in range(n):
            if safe[i][j] == 1:
                count += 1
                dfs(i, j)
    return count

max_num = 0
counts = []
for i in range(n):
    temp_num = max(grid[i])
    if max_num < temp_num:
        max_num = temp_num
if max_num == 1:
    print(1)
    exit()
for i in range(0,max_num):
    counts.append(make_safeArea(i+1))
print(max(counts))