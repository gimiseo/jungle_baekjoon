import sys
input = sys.stdin.readline

yesnolist = []

def isVPS(vps_str):
    global yesnolist
    result = vps_str
    while result.count("()"):
        result = result.replace("()", "")
    if result:
        yesnolist.append("NO")
    else:
        yesnolist.append("YES")



num = int(input())
for _ in range(num):
    isVPS(input().rstrip())
print("\n".join(yesnolist))