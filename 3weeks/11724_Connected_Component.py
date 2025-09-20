from collections import deque
#인자받기
n, m = map(int, input().split())
graph = [[]*(n) for _ in range(n)]
#bfs
def bfs(start):
    que = deque()
    que.append(start + 1)
    visited[start] = True
    while que:
        cur = que.popleft()
        for a in graph[cur - 1]:
            if visited[a - 1] == False:
                que.append(a)
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
start = 0
count = 0
while not all_found_stwitch:
    cur = start
    bfs(cur)
    count += 1
    if False not in visited:
        all_found_stwitch = True
    else:
        for i, a in enumerate(visited):
            if a == False:
                start = i
print(count)