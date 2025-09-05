#하 라면서 골드 5문제 던져주는 정글
#원반의 이동횟수 f(n) = 1 + 2f(n-1) -> 2 ** n -1
#재귀호출 레츠기릿
#시작에서 임시로 가는 재귀호출
#임시에서 목표로 가는 재귀호출 하나

def hanoi(num, start, temp, to):
    #이것이... 재귀의 종료
    if num == 1:
        print(f"{start} {to}")
        return
    hanoi(num-1,start,to,temp)
    print(f"{start} {to}")
    hanoi(num-1,temp,start,to)

n = int(input())
print(2**n - 1)
if n <= 20:
    hanoi(n, 1, 2, 3)