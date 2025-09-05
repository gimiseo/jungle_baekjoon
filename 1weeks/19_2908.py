#s = "hello"
#reversed_s = s[::-1]  # 결과: "olleh" 문자열을 뒤집는 방...법

num1, num2 = map(int, input()[::-1].split())

if num1 > num2:
    print(num1)
else:
    print(num2)