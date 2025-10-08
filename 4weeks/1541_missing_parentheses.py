from collections import deque

str = input()
str_len = len(str)
minus_flag = False

def mini_atoi():
    num = 0
    while num_str:
        cur_n = int(num_str.popleft())
        num = num*10 + cur_n
    if minus_flag:
        num = -num
    return num

result = 0
num_str = deque()
for i in range(str_len):
    if str[i] == '-' or str[i] == '+':
        result += mini_atoi()
        if str[i] == '-' and not minus_flag:
            minus_flag = True
        
    else:
        num_str.append(str[i])
result += mini_atoi()
print(result)