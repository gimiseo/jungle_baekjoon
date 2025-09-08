#x if a > b else y -> 파이썬에서 삼항연산자 쓰는법 기존 -> a > b ? x : y;
#로직 사고흐름
#9개. 더한다.
#2개씩 빼서. 더한다.
#값이. 100이. 나온.다
#야호 성공

talls = []
temp = []
for _ in range(9):
    talls.append(int(input()))
for i in range(9):
    for j in range(i+1, 9):
        temp = talls[:]
        temp.pop(i), temp.pop(j - 1)
        if sum(temp) == 100:
            temp.sort()
            for a in temp:
                print(a)
            exit()