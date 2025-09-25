#값 받기
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
reversed_graph = [[] for _ in range(n+1)]
count = 0

for _ in range(m):
    heavier, lighter = map(int, input().split())
    graph[heavier].append(lighter)
    reversed_graph[lighter].append(heavier)
for a in graph:
    if len(a) >= (n+1)//2:
        count += 1
for b in reversed_graph:
    if len(b) >= (n+1)//2:
        count += 1
print(count)