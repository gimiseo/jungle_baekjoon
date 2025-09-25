INF = int(1e9)  # 엄청 큰 수 = 못 가는 거리

# 1. 노드 개수: 3명 (1번, 2번, 3번)
n = 3

# 2. 거리 배열 만들기 (초기값: 전부 못 가는 상태)
d = [[INF] * (n + 1) for _ in range(n + 1)]

# 3. 자기 자신까지는 0분 (자기한테 편지 주는 건 0초)
for i in range(1, n + 1):
    d[i][i] = 0

# 4. 직접 연결된 친구들 거리 입력 (간선 정보)
d[1][2] = 3   # 1 → 2 : 3분
d[2][3] = 2   # 2 → 3 : 2분
d[1][3] = 10  # 1 → 3 : 10분

# 5. 플로이드-워셜 알고리즘
for m in range(1, n + 1):       # 중간에 거쳐갈 친구
    for s in range(1, n + 1):   # 시작 친구
        for e in range(1, n + 1):  # 끝 친구
            if d[s][e] > d[s][m] + d[m][e]:
                d[s][e] = d[s][m] + d[m][e]

# 6. 최종 결과 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if d[i][j] == INF:
            print(f"{i} → {j}: 못 감")
        else:
            print(f"{i} → {j}: {d[i][j]}분")
