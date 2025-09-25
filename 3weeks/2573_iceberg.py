from collections import deque

def inRange(x, y):
    if x in range(0, n) and y in range(0, m):
        return True
    else:
        return False

def find_and_count_ice(x,y):
    first_find_flag = False
    count = 0
    ice_x, ice_y = (0,0)
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if grid[i][j] != 0:
                if first_find_flag == False:
                    ice_x, ice_y = i, j
                    first_find_flag = True
                count += 1
    return (ice_x, ice_y, count)

def bfs_and_melt(x,y):
    ice_count = 1
    q = deque()
    q.append((x,y))
    visited[x][y] = 1

    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nex_x, nex_y = cur_x + dxs[i], cur_y + dys[i]
            if grid[nex_x][nex_y] == 0 and grid[cur_x][cur_y] > 0 and visited[nex_x][nex_y] != 1:
                grid[cur_x][cur_y] -= 1
            if grid[nex_x][nex_y] != 0 and visited[nex_x][nex_y] != 1:
                q.append((nex_x,nex_y))
                visited[nex_x][nex_y] = 1
                ice_count += 1
    return ice_count
            


#인접행렬 테크닉 상하좌우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

#문제, 빙산이 분리되는 최초의 시간을 출력
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

years = 0
while True:
    visited = [[0 for _ in range(m)] for _ in range(n)]
    first_x, first_y, ice_count = find_and_count_ice(1,1)
    if ice_count == 0:
        years = 0
        break
    if bfs_and_melt(first_x,first_y) != ice_count:
        break
    years += 1

print(years)