# 어떤 구슬 x에 대해
# x보다 무거운 구슬이 (N+1)/2개 이상이면 → ❌ 중간 못 됨
# x보다 가벼운 구슬이 (N+1)/2개 이상이면 → ❌ 중간 못 됨

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