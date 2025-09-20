from collections import deque
#연결요소문제하고 똑띠

#인자받기
n = int(input())
m = int(input())
graph = [[]*(n) for _ in range(n)]

#bfs
def bfs(start):
    global count
    que = deque()
    que.append(start)
    visited[start - 1] = True
    while que:
        cur = que.popleft()
        for a in graph[cur - 1]:
            if visited[a - 1] == False:
                que.append(a)
                count += 1
                visited[a - 1] = True
#all_found switch
all_found_stwitch = False
#visited
visited = [False] * n

#그래프 채우기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b)
    graph[b - 1].append(a)
count = 0
bfs(1)
print(count)