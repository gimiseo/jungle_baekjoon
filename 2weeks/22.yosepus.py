from collections import deque

n, k = map(int, input().split())
queue = deque()
for i in range(n):
    queue.append(i+1)

answer = []
count = 0
while queue:
    count += 1
    if count == k:
        count = 0
        answer.append(queue.popleft())
    else:
        queue.append(queue.popleft())
formatted = "<" + ", ".join(map(str, answer)) + ">"
print(formatted)

# count, 한다. 3번때 팝, 한다. 아니면 뒤로 보낸다. 컨테이너 시작이다아아아아
# 생각의 흐름
# 아 뭐야 쉽잖아...