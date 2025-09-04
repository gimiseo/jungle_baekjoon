A = int(input())
B = int(input())
C = int(input())

abc = A*B*C
num_list = []
while abc > 0:
    num_list.append(abc%10)
    abc=abc//10
for i in range(10):
    print(num_list.count(i))
    