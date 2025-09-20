# from collections import deque

# #인자받기
# n = int(input())
# graph = [[] for _ in range(n)]

# #walk_bfs
# def walk_bfs(start):
#     visited = [False] * n
#     global count
#     que = deque()
#     que.append(start)
#     visited[start - 1] = True
#     # 규칙1 실내일 경우에만 que에 넣는다
#     # 규칙2 실외일 경우 count + 1 하고 넣지않는다.
#     while que:
#         cur = que.popleft()
#         for a in graph[cur - 1]:
#             if visited[a - 1] == False and in_and_out[a-1] == 0:
#                 que.append(a)
#                 visited[a - 1] = True
#             elif visited[a - 1] == False and in_and_out[a-1] == 1:
#                 count +=1

# #all_found switch
# all_found_stwitch = False
# #visited

# s = input()
# in_and_out = list(map(int, s))

# #그래프 채우기
# for _ in range(n - 1):
#     a, b = map(int, input().split())
#     graph[a - 1].append(b)
#     graph[b - 1].append(a)
# count = 0
# for i in range(n):
#     if in_and_out[i] == 1:
#         walk_bfs(i + 1)
# print(count)

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()
in_and_out = list(map(int, s))

graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    graph[a].append(b)
    graph[b].append(a)

count = 0
# 1. 실내-실내 직접 연결
for i in range(n):
    if in_and_out[i] == 1:
        for nb in graph[i]:
            if in_and_out[nb] == 1:
                count += 1

# 2. 실외 컴포넌트 탐색
visited = [False] * n
for i in range(n):
    if in_and_out[i] == 0 and not visited[i]:
        que = deque([i])
        visited[i] = True
        indoor_neighbors = set()
        while que:
            cur = que.popleft()
            for nb in graph[cur]:
                if in_and_out[nb] == 0 and not visited[nb]:
                    visited[nb] = True
                    que.append(nb)
                elif in_and_out[nb] == 1:
                    indoor_neighbors.add(nb)
        k = len(indoor_neighbors)
        count += k * (k - 1)

print(count)
