n = int(input())
stack = []
for _ in range(n):
    order = input()
    if order[0:4] == "push":
        push, num = order.split()
        stack.append(int(num))
    elif order == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif order == "top":
        if stack:
            temp = stack.pop()
            print(temp)
            stack.append(temp)
        else:
            print(-1)
        