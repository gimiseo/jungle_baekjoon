#차이가 큰걸 만날때까지 -> 
#정렬이 필요할까? 

from collections import deque

def absolute(n):
    if n < 0:
        value = -n
    else:
        value = n
    return value

n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
dq = deque(num_list)
result_list = []
flag = True

while dq:
    if len(dq) == 1 and not flag:
        result_list.insert(0,dq.pop())
    elif flag:
        result_list.append(dq.pop())
        flag = False
    else:
        result_list.append(dq.popleft())
        flag = True

max = 0
for i in range(len(result_list) - 1):
    max += absolute(result_list[i] - result_list[i + 1])
print(max)