import sys
input = sys.stdin.readline

yesnolist = []

def isVPS(vps_str):
    global yesnolist
    stack = []
    result = vps_str
    for i in range(len(result)):
        if result[i] == "(":
            stack.append("(")
        elif result[i] == ")":
            if stack:
                stack.pop()
            else:
                yesnolist.append("NO")
                return
    if stack:
        yesnolist.append("NO")
    else:
        yesnolist.append("YES")
    


num = int(input())
for _ in range(num):
    isVPS(input().rstrip())
print("\n".join(yesnolist))