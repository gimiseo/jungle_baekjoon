from collections import deque

def inRange(x, y):
    if x in range(0, n) and y in range(0, m):
        return True
    else:
        return False

def bfs(x, y):
    visited = [[0] * m for _ in range(n)]
    queue = deque([(x,y)])
    visited[x][y] = 1
    while queue:
        cur_x, cur_y = queue.popleft()
        if (cur_x, cur_y) == (n - 1, m - 1):
            return visited[cur_x][cur_y]
        for i in range(4):
            nex_x, nex_y = cur_x + dxs[i], cur_y + dys[i]
            if inRange(nex_x, nex_y) and grid[nex_x][nex_y] != 0 and visited[nex_x][nex_y] == 0:
                queue.append((nex_x, nex_y))
                visited[nex_x][nex_y] = visited[cur_x][cur_y] + 1
    

n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

print(bfs(0,0))