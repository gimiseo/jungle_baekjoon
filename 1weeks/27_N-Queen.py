
# # #유명한 문제지만, 머리 박으면 풀릴것같아서 풀어본다.
# # #첫번째 생각 퀸을 놓는순간 놓으면 안되는 자리를 1로 전부 표시한다.
# # #다음자리로 재귀를 타고
# # #시간 타임 이슈
# # #백준에서 N-Queen을 풀 때는 보드를 매번 복사하지 않고,
# # #열/대각선 사용 여부만 체크하는 방식으로 최적화해야 합니다.

# def inRange(x, y):
#     if x in range(0, n) and y in range(0, n):
#         return True
#     else:
#         return False

# #queen_force생성 완료ㅠㅠㅠ
# def make_queenforce(x, y):
#     global chessboard
#     diag_x = [-1, 1, 1 , -1]
#     diag_y = [-1, -1, 1 , 1]
#     for i in range(n):
#         chessboard[x][i] += 1
#         chessboard[i][y] += 1
#     chessboard[x][y] -= 1
#     for i in range(4):
#         cur_x, cur_y = x, y
#         while True:
#             cur_x, cur_y = cur_x + diag_x[i], cur_y + diag_y[i]
#             if not inRange(cur_x, cur_y):
#                 break
#             chessboard[cur_x][cur_y] += 1

# def delete_queenforce(x, y):
#     global chessboard
#     diag_x = [-1, 1, 1 , -1]
#     diag_y = [-1, -1, 1 , 1]
#     for i in range(n):
#         chessboard[x][i] -= 1
#         chessboard[i][y] -= 1
#     chessboard[x][y] += 1
#     for i in range(4):
#         cur_x, cur_y = x, y
#         while True:
#             cur_x, cur_y = cur_x + diag_x[i], cur_y + diag_y[i]
#             if not inRange(cur_x, cur_y):
#                 break
#             chessboard[cur_x][cur_y] -= 1
            
# def start_set_queen(start):
#     global count, chessboard
#     if start >= n:
#         count += 1
#         return
#     for i in range(n):
#         if chessboard[start][i] == 0:
#             make_queenforce(start, i)
#             start_set_queen(start + 1)
#             delete_queenforce(start, i)
# n = int(input())
# count = 0
# chessboard = [[0 for _ in range(n)] for _ in range(n)]
# start_set_queen(0)
# print(count)

#복잡도 이슈. 
# 지금 생각든게 줄이고 줄이고
#어차피 행은 필요가 없음. 그 행을 찍을 필요없음
#그리고 그 열 위치, 대각선 위치를 특정할수있으므로 그리고 r+c으로 나올수있는 조합은 7가지라는 점을 이용
#문제해결!!
def count_queen(n):
    cols = [False]*n
    diag1 = [False]*(2*n-1)
    diag2 = [False]*(2*n-1)
    result = 0
    def dfs(r):
        nonlocal result
        if r == n:
            result += 1
            return
        for c in range(n):
            if not cols[c] and not diag1[r+c] and not diag2[r-c+n-1]:
                cols[c] = diag1[r+c] = diag2[r-c+n-1] = True
                dfs(r+1)
                cols[c] = diag1[r+c] = diag2[r-c+n-1] = False
    dfs(0)
    return result
n = int(input())
print(count_queen(n))