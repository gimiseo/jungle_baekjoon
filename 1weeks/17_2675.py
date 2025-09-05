#문제요구사항 -> 문자열 s를 받는다. ->각 문자를 R번 반복해 새 문자열 p를 만들...?
num = int(input())
for _ in range(num):
    repeat, str = input().split()
    repeat= int(repeat)
    for i in range(len(str)):
        print(str[i]*repeat, end="")
    print()