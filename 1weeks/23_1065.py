#이것도 수식으로 접근해야겠죠....하핫
#등차수열 = 연속하는 두 항의 차이가 모두 일정한 수열
#가우스 공식 -> 등차수열은 앞과 끝단의 합이 일정하다.

def is_han(num):
    if num // 10 == 0 or num //100 == 0:
        return True
    num_list = []
    sum = 0
    while num > 0:
        num_list.append(num%10)
        num //= 10
    diff = num_list[0] - num_list[1]
    prev = num_list.pop()
    while num_list:
        curr = num_list.pop()
        if diff != curr - prev:
            return False
        prev = curr
    return True

in_num = int(input())

if in_num < 100:
    print(in_num)
    exit()
count = 99
for n in range(100, in_num + 1):
    if is_han(n):
        count += 1
print(count)