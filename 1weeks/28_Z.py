
#어떻게 짰는지도 모르겠다 너무졸려...

# def next_go(n, c):
#     global move_count
#     next_x = [1-2**n, 1]
#     next_y = [1, -(2**n+1)]
#     if move_count % 4 != 0 or move_count == 0:
#         if  c == "x":
#             return next_x[0]
#         else:
#             xy_flag = False
#             return next_y[0]
#     else:
#         if  c == "x":
#             return next_x[1]
#         else:
#             xy_flag = True
#             return next_y[1]
# next_go(n,"x")
# next_go(n,"y")

#z자가.... 보인다...!
import sys

dx = [0, 1, 0] 
dy = [1, -1, 1]

def move_z(n):
    global x,y, move_count, ans
    d_x = [-2**(n-1) + 1, 1, -2**(n-1) + 1] 
    d_y = [1, -(2 ** n) + 1, 1]
    if n == 1:
        for i in range(3):
            x = x + dx[i]
            y = y + dy[i]
            move_count += 1
            #board[x][y] = move_count
            if (x,y) == (r,c):
                ans = move_count
        return
    for i in range(4):
        move_z(n-1)
        if i < 3:
            x = x + d_x[i]
            y = y + d_y[i]
            move_count += 1
            #board[x][y] = move_count
            if (x,y) == (r,c):
                ans = move_count

num, r, c = map(int, sys.stdin.readline().split())
# board = [[0 for _ in range(2**num)] for _ in range(2**num)]
move_count = 0
ans = 0
x, y = 0, 0

move_z(num)
print(ans)
#재귀로 하면 백준 통과 안됨 백준 재귀 호출 한도가 1000인데 내 코드는 1398101회 호출함