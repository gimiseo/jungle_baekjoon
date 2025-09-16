import sys
input = sys.stdin.readline

n = int(input())

values = []
for _ in range(n):
    c, r = list(map(int, input().split()))
    values.append(["L", c-r])
    values.append(["R", c+r])
values.sort(key=lambda p: (-p[1], p[0]), reverse=True)

stack = []
count = 1

for value in values:
    if value[0] == "L":
        stack.append(value)
    else:
        cum_width = 0

        while stack:
            prev = stack.pop()

            if prev[0] == "L":
                width = value[1] - prev[1]

                # 너비가 같으면 +2
                if width == cum_width:
                    count += 2
                else:
                    count += 1

                stack.append(["C", width]) 
                break

            # 내부원
            elif prev[0] == "C":
                cum_width += prev[1]
    
print(count)