from collections import deque, defaultdict

def kahn_topo_sort(graph, n):
    indegree = [0] * (n + 1)
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    result = []
    while q:
        node = q.popleft()
        result.append(node)
        for next_node in graph[node]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                q.append(next_node)

    if len(result) != n:
        raise Exception("사이클 존재: 위상 정렬 불가")

    return result


# 👉 DAG 입력 예시 (텍스트로 봤던 구조)
# 5 → 1
# 7 → 1
# 1 → 2, 3
# 3 → 4
# 6 → 8

def main():
    graph = defaultdict(list)
    graph[5] = [1]
    graph[7] = [1]
    graph[1] = [2, 3]
    graph[3] = [4]
    graph[6] = [8]
    graph[2] = []
    graph[4] = []
    graph[8] = []

    n = 8  # 노드 수

    try:
        result = kahn_topo_sort(graph, n)
        print("위상 정렬 결과:", result)
    except Exception as e:
        print("오류 발생:", e)

if __name__ == "__main__":
    main()
