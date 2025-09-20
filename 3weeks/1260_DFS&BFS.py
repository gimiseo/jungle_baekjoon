from collections import deque
# 입력 받기
n, m, v = map(int, input().split())


# 그래프 구성
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 번호 작은 것부터 방문 → 정렬
for node in graph:
    node.sort()

# DFS

def dfs(start):
    visited = [False] * (n + 1)
    stack = []
    stack.append(start)
    while stack:
        cur = stack.pop()
        if visited[cur] == False:
            print(cur, end=" ")
            visited[cur] = True
        for a in reversed(graph[cur]):
            if visited[a] == False:
                stack.append(a)


# BFS
def bfs(start):
    visited = [False] * (n + 1)
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        cur = queue.popleft()
        print(cur, end=" ")
        for a in graph[cur]:
            if visited[a] == False:
                queue.append(a)
                visited[a] = True
# 실행
dfs(v)
print()
bfs(v)