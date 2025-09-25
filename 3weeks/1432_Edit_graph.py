import sys
import heapq

input = sys.stdin.readline

def floyd_warshall(adjmat, N):
    # adjmat[i][j] == 1 이면 i→j 간선 존재
    # 전이 폐쇄 (i→k, k→j 있으면 i→j 설정)
    for k in range(N):
        for i in range(N):
            if adjmat[i][k]:
                for j in range(N):
                    if adjmat[k][j]:
                        adjmat[i][j] = 1

def solve():
    N = int(input().strip())
    adjmat = [list(map(int, list(input().strip()))) for _ in range(N)]
    # 방향 뒤집은 인접 리스트 + 진입 차수 계산
    graph = [[] for _ in range(N)]
    indegree = [0] * N

    for i in range(N):
        for j in range(N):
            if adjmat[i][j] == 1:
                # 원래 간선 i → j 이었음
                # 뒤집어서 저장: j → i
                graph[j].append(i)
                indegree[i] += 1

    # 순환 검사 via 플로이드-워셜
    floyd_warshall(adjmat, N)
    for i in range(N):
        if adjmat[i][i] == 1:
            print(-1)
            return

    # 위상 정렬 (큰 번호 우선)
    # 파이썬 heapq는 최소 힙이므로, 음수로 저장
    heap = []
    for i in range(N):
        if indegree[i] == 0:
            heapq.heappush(heap, -i)  # 음수로 해서 큰 i 가 먼저 나옴

    result = [0] * N
    current_rank = N
    cnt = 0
    while heap:
        x = -heapq.heappop(heap)
        result[x] = current_rank
        current_rank -= 1
        cnt += 1
        for nxt in graph[x]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                heapq.heappush(heap, -nxt)

    # 만약 모든 정점을 처리 못했다면 순환
    if cnt != N:
        print(-1)
    else:
        # 출력: 1번 정점부터 N번 정점까지 등수
        print(" ".join(str(result[i]) for i in range(N)))

if __name__ == "__main__":
    solve()
