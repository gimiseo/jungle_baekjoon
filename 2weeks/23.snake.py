from collections import deque
#방향전환 세팅
dx = [0,1,0,-1]
dy = [1,0,-1,0] #오아래왼위

#outofrange 탈출조건
def inRange(x, y):
    if x in range(1, board_N + 1) and y in range(1, board_N + 1):
        return True
    else:
        return False

board_N = int(input())
board = [[0] * (board_N + 1) for _ in range(board_N+1)]
apple_k = int(input())
for _ in range(apple_k):
    r, c = map(int, input().split())
    board[r][c] = 'a'
chage_event_N = int(input())
chage_s_d = deque()
for _ in range(chage_event_N):
    s, d = map(str, input().split())
    chage_s_d.append((int(s), d))


snake_size = 1
snake = deque([(1,1)])
board[1][1] = 1
cur_d = 0

second = 0

while True:
    second += 1
    haed_x, head_y = snake[-1]
    next_x, next_y = haed_x + dx[cur_d],head_y + dy[cur_d]
    if not inRange(next_x, next_y) :
        break
    if board[next_x][next_y] == 1:
        break
    if board[next_x][next_y] == 'a':
        snake_size += 1
    if chage_s_d and second == chage_s_d[0][0]:
        s, d = chage_s_d.popleft()
        if d == "D":
            cur_d = (cur_d + 1) % 4
        else:
            cur_d = (cur_d + 3) % 4
    snake.append((next_x, next_y))
    board[next_x][next_y] = 1
    while len(snake) > snake_size:
        temp_x, temp_y = snake.popleft()
        board[temp_x][temp_y] = 0
print(second)

#음 그러니까 사실 큐 쓰는게 맞긴하다. 상단 추가 하단 제거
#사과 먹으면 상단 추가 하단 미제거, 현황유지
#그러니까 굳이 각각의 점이 현항을 기억할 필요없이 그냥 족적을 남기다가 남길것지 팝할건지만 정하면 됨
#초 관련해서도 큐로 만들어 놓고 [3, 'D']로 만들고 상단과 비교하면서 -> q[0][0] 그 초면 q[0][1]
#확인하고 어디로 돌지 정하면됨
#내가 dx dy를 쓰겠다고 정했다면 D냐 L이냐에 따라 숫자를 섹시하게 설정할수있으면 좋을텐데
# 방향전환이 매끄럽게 되게위해 두개로 나눴다. 오 왼이냐로 나뉘기 때문에 아마 0이냐 1 이냐로 결정할수있는데 
# 아래냐 위냐에 따라 대처가 매끄러울수있다는 생각
# 큐이므로 이동시 지금 결정된 방향에 따라 생성, 삭제, (뱀의 몸길이 현황에 따라)
#뱀을 만나면 죽는건 또 몰랐네
# 좌냐 우냐 그걸 결정하는 깔쌈한 방법

# 오왼위아래
# 오 일때 오는 아래 왼은 위 		+1 +3
# 아래일때 오는 왼 왼은 오 		    +1+ 3
# 왼 일때 오는 위 왼은 아래		    +1 + 3
# 위 일때 오는 오 왼은 왼		    +1 +3