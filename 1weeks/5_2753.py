year = int(input())

#윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 떄 or 400의 배수
#1900은 100의 배수이고 400배수가 아니니까 윤년이 아니다.
#하지만 2000은 

if (year % 4) == 0:
    if (year % 100) != 0 or (year % 400) == 0:
        print(1)
    else:
        print(0)
else:
    print(0)
